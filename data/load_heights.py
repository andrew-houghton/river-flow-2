import pickle
import bz2
from pathlib import Path


def load():
    with bz2.BZ2File(Path(__file__).parent.joinpath('heights.pbz2'), 'r') as f:
        return pickle.load(f)
