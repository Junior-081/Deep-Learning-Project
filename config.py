import argparse

args=argparse.Namespace(
    lr=1e-4,
    bs=8,
    train_size=0.8,
    path="./data/Images",
    metadata="./data/metadata_ok.csv",
    wd=0.1

)