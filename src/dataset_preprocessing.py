'''
Clean some parts of the dataset to have a more readable text
'''

import numpy as np
import string

from datasets import load_dataset
from tqdm import tqdm

ds = load_dataset("SamuelYang/bookcorpus") # replica TorontoBookCorpus dataset

# things to adjust:
# 1) before punctuation there is always a white space to be removed
# 2) the dataset is composed of row sentences with a . at the end this sentence togheter for the text so i need to remove the point and merge them

filename_dataset = 'data/data.txt'

# get new info on the adjusted dataset
num_words = 0
set_unique_words, num_unqiue_words = set(), 0
num_words_per_sentence_mean = 0
all_word_counts, num_words_per_sentence_median = [], 0
size_byte = 0

for feature in tqdm(ds['train']):
    sentence = feature['text']
    words = sentence.split()
    words = words[:-1] if words[-1] == '.' else words

    new_sentence = ''

    for i, word in enumerate(words):
        if word in string.punctuation:
            new_sentence = new_sentence.rstrip() + word + ' ' if i != len(words) - 1 else new_sentence.rstrip() + word
        else:
            new_sentence += word + ' ' if i != len(words) - 1 else word

    num_words += len(new_sentence.split())
    set_unique_words.update(w.lower() for w in new_sentence.split())
    all_word_counts.append(len(new_sentence.split()))
    size_byte += len(new_sentence.encode('utf-8'))

    with open(filename_dataset, 'a') as f:
        f.write(new_sentence + ' ')

num_unique_words = len(set_unique_words)
num_words_per_sentence_mean = num_words / 74004228 # num sentences is the second number that didn't changed
num_words_per_sentence_median = np.median(all_word_counts)

print(f"Number of words: {num_words}")
print(f"Number of unique words: {num_unqiue_words}")
print(f"Words per sentence (mean): {num_words_per_sentence_mean}")
print(f"Words per sentence (median): {num_words_per_sentence_median}")
print(f"Size in GB: {size_byte / (1024 ** 3):2f}")

# number of books: 11,038 ?
# number of sentences: 74,004,228 v
# number of words: 984,846,357 x
# number of unique words: 1,316,420 x
# number of words per sentence (mean): 13 v
# number of words per sentence (median): 11 v