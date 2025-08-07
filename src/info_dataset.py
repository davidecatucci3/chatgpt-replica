'''
I want to extrapolat info from replica of TorontoBookCorpus dataset to see if they are similar or not
'''

import numpy as np

from datasets import load_dataset
from tqdm import tqdm

ds = load_dataset("SamuelYang/bookcorpus") # replica TorontoBookCorpus dataset

# data from TorontoBookCorpus dataset (now is not available so i am downloading a replica)
# if there is a x data do not correspond with downloaded dataset and if there is ? that means that i cannot check and if there is v data corresponds
# number of books: 11,038 ?
# number of sentences: 74,004,228 v
# number of words: 984,846,357 x
# number of unique words: 1,316,420 x
# number of words per sentence (mean): 13 v
# number of words per sentence (median): 11 v

num_words, num_expected_words = 0, 984846357
set_unique_words, num_unqiue_words, num_expected_unique_words = set(), 0, 1316420
num_words_per_sentence_mean, num_expected_words_per_sentence_mean = 0, 13
all_word_counts, num_words_per_sentence_median, num_expected_words_per_sentence_median = [], 0, 11
num_sentences = 0
size_byte = 0

for feature in tqdm(ds['train']):
    sentence = feature['text']
    words = sentence.split()

    num_sentences += 1
    size_byte += len(sentence.encode('utf-8'))
    num_words += len(words)
    set_unique_words.update(w.lower() for w in words)
    all_word_counts.append(len(words))
    
num_unique_words = len(set_unique_words)
num_words_per_sentence_mean = num_words / num_sentences
num_words_per_sentence_median = np.median(all_word_counts)

print(f"Number of words: Equal: {num_words == num_expected_words} | Numbers: {num_words, num_expected_words} | Error: {abs(num_words - num_expected_words)}")
print(f"Number of unique words: {num_unique_words == num_expected_unique_words} | Numbers: {num_unique_words, num_expected_unique_words} | Error: {abs(num_unique_words - num_expected_unique_words)}")
print(f"Words per sentence (mean): {num_words_per_sentence_mean == num_expected_words_per_sentence_mean} | Numbers: {num_words_per_sentence_mean, num_expected_words_per_sentence_mean} | Error: {abs(num_words_per_sentence_mean - num_expected_words_per_sentence_mean)}")
print(f"Words per sentence (median): {num_words_per_sentence_median == num_expected_words_per_sentence_median} | Numbers: {num_words_per_sentence_median, num_expected_words_per_sentence_median} | Error: {abs(num_words_per_sentence_median - num_expected_words_per_sentence_median)}")
print(f"Size in GB: {size_byte / (1024 ** 3):2f}")