from typing import Literal
import pandas as pd
import torch
import torchaudio
import torchaudio.transforms as T


class RIRDataset:
    """
    Class for RIR augmentation. Contains a pandas dataframe with the filepaths. Can be randomly sampled from.
    """

    def __init__(self, config):
        self.config = config

        self.rir_root = config["rir_root"]
        pointsource_df = pd.read_csv(
            self.rir_root + "RIRS_NOISES/pointsource_noises/noise_list", sep=" ", header=None
        ).iloc[
            :, -1
        ]  # Get the last column that contains the filepaths
        isotropic_df = pd.read_csv(
            self.rir_root + "RIRS_NOISES/real_rirs_isotropic_noises/noise_list", sep=" ", header=None
        ).iloc[
            :, -1
        ]  # Get the last column that contains the filepaths
        self.df = pd.concat([pointsource_df, isotropic_df], axis=0)

        # print(f"Loaded {len(self.df)} RIRs.")
        # print(self.df.head())

    def __len__(self):
        return len(self.df)

    def get_random_rir(self):
        path = self.rir_root + self.df.sample(1).iloc[0]
        try:
            rir = torchaudio.load(path)[0]
        except Exception as e:
            print(f"Failed to load RIR from {path}.")
            raise e
        if rir.size(0) > 1:
            rir = rir.mean(0)
        return rir.squeeze().unsqueeze(0)


class RIRAugmentations:
    """
    Class for RIR augmentations.
    """

    def __init__(
        self, config, sample_rate: int = 16000, device="cuda" if torch.cuda.is_available() else "cpu"
    ):
        self.device = device
        self.sample_rate = sample_rate
        self.rir_dataset = RIRDataset(config)

        self.convolver = T.Convolve().to(self.device)

    def apply_rir(
        self,
        waveform: torch.Tensor,
        method: Literal["convolve", "superimpose"] = "superimpose",
        scale_factor: float = 0.5,
    ) -> torch.Tensor:
        """
        Apply a random RIR to the audio waveform.

        param waveform: The audio waveform to apply the RIR to.
        param method: The method to apply the RIR with. Can be "convolve" or "superimpose".
        param scale_factor: The scale factor to apply to the RIR, should be between 0.2 and 0.8.

        return: The audio waveform with the RIR applied.
        """
        waveform = waveform.to(self.device)
        rir = self.rir_dataset.get_random_rir().to(self.device)
        if method == "convolve":
            wf = self.convolver(waveform, rir * scale_factor)
            return wf / torch.max(torch.abs(wf))
        elif method == "superimpose":
            # Cut or pad the RIR to match the waveform length
            if waveform.size(1) > rir.size(1):
                rir = torch.nn.functional.pad(rir, (0, waveform.size(1) - rir.size(1)))
            elif waveform.size(1) < rir.size(1):
                rir = rir[:, : waveform.size(1)]
            wf = waveform + rir * scale_factor
            return wf / torch.max(torch.abs(wf))
