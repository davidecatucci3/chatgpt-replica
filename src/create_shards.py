'''
Create shards (numpy files that contains chunk of text tokenized, it is faster to retrieve during training time)
'''

import numpy as np

from datasets import load_dataset
from tqdm import tqdm

ds = load_dataset("SamuelYang/bookcorpus") # replica TorontoBookCorpus dataset
