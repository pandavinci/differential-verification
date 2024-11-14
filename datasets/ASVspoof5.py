from typing import Literal
import torch
from torch.utils.data import Dataset
from torchaudio import load
import os
import pandas as pd
import numpy as np

from augmentation.augment import augment_waveform


class ASVspoof5Dataset_base(Dataset):
    """
    Base class for the ASVspoof5 dataset. This class should not be used directly, but rather subclassed.

    param root_dir: Path to the ASVspoof5 folder
    param protocol_file_name: Name of the protocol file to use
    param variant: One of "train", "dev", "eval" to specify the dataset variant
    """

    def __init__(self, root_dir, protocol_file_name, variant: Literal["train", "dev", "eval"] = "train", augment=False):
        self.augment = False if variant == "train" else augment
        
        self.root_dir = root_dir

        protocol_file = os.path.join(self.root_dir, protocol_file_name)
        self.protocol_df = pd.read_csv(protocol_file, sep=" ", header=None)

        subdir = ""
        if variant == "train":
            subdir = "flac_T"
            self.protocol_df.columns = ["SPEAKER_ID", "AUDIO_FILE_NAME", "GENDER", "-", "SYSTEM_ID", "KEY"]
        elif variant == "dev":
            subdir = "flac_D"
            self.protocol_df.columns = ["SPEAKER_ID", "AUDIO_FILE_NAME", "GENDER", "-", "SYSTEM_ID", "KEY"]
        elif variant == "eval":
            subdir = "flac_E_prog"
            self.protocol_df.columns = ["AUDIO_FILE_NAME"]
        self.rec_dir = os.path.join(self.root_dir, subdir)

    def __len__(self):
        return len(self.protocol_df)

    def __getitem__(self, idx):
        raise NotImplementedError("This method should be implemented in a specific subclass")

    def get_labels(self) -> np.ndarray:
        """
        Returns an array of labels for the dataset, where 0 is genuine speech and 1 is spoofing speech
        Used for computing class weights for the loss function and weighted random sampling (see train.py)
        """
        return self.protocol_df["KEY"].map({"bonafide": 0, "spoof": 1}).to_numpy()

    def get_class_weights(self):
        """Returns an array of class weights for the dataset, where 0 is genuine speech and 1 is spoofing speech"""
        labels = self.get_labels()
        class_counts = np.bincount(labels)
        class_weights = 1.0 / class_counts
        return torch.FloatTensor(class_weights)


class ASVspoof5Dataset_pair(ASVspoof5Dataset_base):
    """
    Dataset class for ASVspoof5 that provides pairs of genuine and tested speech for differential-based detection.
    """

    def __init__(self, root_dir, protocol_file_name, variant: Literal["train", "dev", "eval"] = "train"):
        super().__init__(root_dir, protocol_file_name, variant)

    def __getitem__(self, idx):
        """
        Returns tuples of the form (test_audio_file_name, gt_waveform, test_waveform, label)
        """
        if torch.is_tensor(idx):
            idx = idx.tolist()

        speaker_id = self.protocol_df.loc[idx, "SPEAKER_ID"]

        test_audio_file_name = self.protocol_df.loc[idx, "AUDIO_FILE_NAME"]
        test_audio_name = os.path.join(self.rec_dir, f"{test_audio_file_name}.flac")
        test_waveform, _ = load(test_audio_name)

        label = self.protocol_df.loc[idx, "KEY"]
        label = 0 if label == "bonafide" else 1

        # Get the genuine speech of the same speaker for differentiation
        speaker_recordings_df = self.protocol_df[
            (self.protocol_df["SPEAKER_ID"] == speaker_id) & (self.protocol_df["KEY"] == "bonafide")
        ]
        if speaker_recordings_df.empty:
            raise Exception(f"Speaker {speaker_id} genuine speech not found in protocol file")

        # Get a random genuine speech of the speaker using sample()
        gt_audio_file_name = speaker_recordings_df.sample(n=1).iloc[0]["AUDIO_FILE_NAME"]
        gt_audio_name = os.path.join(self.rec_dir, f"{gt_audio_file_name}.flac")
        gt_waveform, _ = load(gt_audio_name)
        
        if self.augment:
            test_waveform = augment_waveform(test_waveform)
            gt_waveform = augment_waveform(gt_waveform)

        return test_audio_file_name, gt_waveform, test_waveform, label


class ASVspoof5Dataset_single(ASVspoof5Dataset_base):
    """
    Dataset class for ASVspoof5 that provides single audio files for "normal" classification.
    """

    def __init__(self, root_dir, protocol_file_name, variant: Literal["train", "dev", "eval"] = "train"):
        super().__init__(root_dir, protocol_file_name, variant)
        self.variant = variant

    def __getitem__(self, idx):
        """
        Returns tuples of the form (audio_file_name, waveform, label)
        """
        if torch.is_tensor(idx):
            idx = idx.tolist()

        audio_file_name = self.protocol_df.loc[idx, "AUDIO_FILE_NAME"]
        audio_name = os.path.join(self.rec_dir, f"{audio_file_name}.flac")
        waveform, _ = load(audio_name)

        if self.variant == "eval":  # No labels for eval set
            label = None
        else:  # 0 for genuine speech, 1 for spoofing speech
            label = 0 if self.protocol_df.loc[idx, "KEY"] == "bonafide" else 1

        if self.augment:
            waveform = augment_waveform(waveform)

        return audio_file_name, waveform, label
