import pickle
import bz2
from pathlib import Path


def load(file):
    with bz2.BZ2File(Path(__file__).parent.joinpath(file+'.pbz2'), 'r') as f:
        return pickle.load(f)
