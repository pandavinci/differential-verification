local_config = {
    "argv": ["--local"],
    "data_dir": "/mnt/d/VUT/Deepfakes/Datasets/",
    "rir_root": "/mnt/d/VUT/Deepfakes/Datasets/RIR/",
    "asvspoof2019la": {
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "LA",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "ASVspoof2019.LA.cm.eval.trl.txt",
    },
    "asvspoof2021la": {
        # need to take train and dev from 2019 and eval from 2021
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "asvspoof2021/LA",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "asvspoof2021df": {
        "train_subdir": "LA",
        "dev_subdir": "asvspoof2021/DF",
        "eval_subdir": "asvspoof2021/DF",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "trial_metadata.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "inthewild": {
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "InTheWild",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "meta.csv",
    },
    "morphing": {
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "Morphing",
        "train_protocol": "train_protocol.txt",
        "dev_protocol": "dev_protocol.txt",
        "eval_protocol": "protocol.txt",
    },
    "asvspoof5": {
        "train_subdir": "ASVspoof5",
        "dev_subdir": "ASVspoof5",
        "eval_subdir": "ASVspoof5",
        "train_protocol": "ASVspoof5.train.metadata.txt",
        "dev_protocol": "ASVspoof5.dev.metadata.txt",
        "eval_protocol": "ASVspoof5.eval.metadata.txt",
    },
    "batch_size": 16,
    "lstm_batch_size": 8,
    "num_epochs": 1,
}

metacentrum_config = {
    "argv": ["--metacentrum"],
    "data_dir": "./",
    "rir_root": "/storage/brno2/home/vojteskas/deepfakes/datasets/",
    "asvspoof2019la": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "LA19",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "ASVspoof2019.LA.cm.eval.trl.txt",
    },
    "asvspoof2021la": {
        # need to take train and dev from 2019 and eval from 2021
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "LA21",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "asvspoof2021df": {
        "train_subdir": "LA19",
        "dev_subdir": "DF21",
        "eval_subdir": "DF21",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "trial_metadata.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "inthewild": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "InTheWild",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "meta.csv",
    },
    "morphing": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "Morphing",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "protocol.txt",
    },
    "asvspoof5": {
        "train_subdir": "",
        "dev_subdir": "",
        "eval_subdir": "",
        "train_protocol": "ASVspoof5.train.metadata.txt",
        "dev_protocol": "ASVspoof5.dev.metadata.txt",
        "eval_protocol": "ASVspoof5.track_1.progress.trial.txt",
    },
    "batch_size": 32,
    "lstm_batch_size": 16,
    "num_epochs": 20,
}

sge_config = {
    "argv": ["--sge"],
    "data_dir": "/mnt/matylda0/istanek/datasets/",
    "rir_root": "/mnt/matylda0/istanek/datasets/",
    "asvspoof2019la": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "LA19",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "ASVspoof2019.LA.cm.eval.trl.txt",
    },
    "asvspoof2021la": {
        # need to take train and dev from 2019 and eval from 2021
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "LA21",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "asvspoof2021df": {
        "train_subdir": "LA19",
        "dev_subdir": "DF21",
        "eval_subdir": "DF21",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "trial_metadata.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "inthewild": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "InTheWild",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "meta.csv",
    },
    "morphing": {
        "train_subdir": "LA19",
        "dev_subdir": "LA19",
        "eval_subdir": "Morphing",
        "train_protocol": "ASVspoof2019.LA.cm.train.trl.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "protocol.txt",
    },
    "asvspoof5": {
        "train_subdir": "",
        "dev_subdir": "",
        "eval_subdir": "",
        "train_protocol": "ASVspoof5.train.metadata.txt",
        "dev_protocol": "ASVspoof5.dev.metadata.txt",
        "eval_protocol": "ASVspoof5.track_1.progress.trial.txt",
    },
    "batch_size": 32,
    "lstm_batch_size": 16,
    "num_epochs": 20,
}
