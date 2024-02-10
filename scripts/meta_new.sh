#!/bin/bash
#PBS -N GMMDiff
#PBS -q gpu@meta-pbs.metacentrum.cz
#PBS -l select=1:ncpus=4:mem=64gb:ngpus=1:gpu_mem=8gb:scratch_ssd=100gb
#PBS -l walltime=24:00:00
#PBS -m ae

export OMP_NUM_THREADS=$PBS_NUM_PPN

cd "$SCRATCHDIR" || exit 1
mkdir TMPDIR
export TMPDIR=$SCRATCHDIR/TMPDIR
DATADIR=/storage/brno2/home/vojteskas

module add gcc
module add conda-modules-py37
conda create -n DP python=3.10 -y
conda activate DP

conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y

cp $DATADIR/DP/dp.zip .
unzip dp.zip

pip install -r requirements.txt --cache-dir "$TMPDIR"

cp -r $DATADIR/deepfakes/datasets/LA.zip .
unzip LA.zip >/dev/null 2>&1

chmod 755 ./*.py

./train_and_eval.py --metacentrum

rm -rf ./*__pycache__*
zip -r GMMDiffResults.zip \
    classifiers datasets embeddings feature_processors trainers \
    config.py train_and_eval.py requirements.txt \
    ./*.png ./*.pt \
    >/dev/null 2>&1
cp GMMDiffResults.zip $DATADIR/DP/GMMDiffResults.zip

clean_scratch
