local_config = {
    "argv": ["--local"],
    "device": "cuda",
    "data_dir": "/mnt/e/VUT/Deepfakes/Datasets/",
    "asvspoof2019la": {
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "LA",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "ASVspoof2019.LA.cm.eval.trl.txt",
    },
    "asvspoof2021la": {
        # need to take train and dev from 2019 and eval from 2021
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "asvspoof2021/LA",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "asvspoof2021df": {
        "train_subdir": "LA",
        "dev_subdir": "LA",
        "eval_subdir": "asvspoof2021/DF",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "batch_size": 16,
    "num_epochs": 1,
}

metacentrum_config = {
    "argv": ["--metacentrum"],
    "device": "cuda",
    "data_dir": "./",
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
        "dev_subdir": "LA19",
        "eval_subdir": "DF21",
        "train_protocol": "ASVspoof2019.LA.cm.train.trn.txt",
        "dev_protocol": "ASVspoof2019.LA.cm.dev.trl.txt",
        "eval_protocol": "trial_metadata.txt",
    },
    "batch_size": 32,
    "num_epochs": 10,
}
