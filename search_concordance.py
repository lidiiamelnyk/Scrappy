#! /usr/bin/env python
# -*- coding: utf-8 -*-


import nltk
from nltk.collocations import *
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.collocations import TrigramAssocMeasures
import re
import pprint
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import Text
import codecs
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import BracketParseCorpusReader
import os, sys, os.path
import shutil
from nltk.probability import FreqDist
import math
import matplotlib
import collections
import json

words_list = []
with codecs.open("words.txt", "r", encoding = 'utf-8') as f:
	for line in f:
		words_list.extend(line.split())

corpus_root = 'C:/Users/Maximilian Schwenke/brickset-scraper/results/'
training_corpus = PlaintextCorpusReader(corpus_root, ".*txt")
#print (len(training_corpus.words()))
#print (len(set(training_corpus.words())))

myText = nltk.Text(training_corpus.words())
training_ngrams = nltk.ngrams((w.lower() for w in training_corpus.words() if w in words_list), 2)
#print(list(training_ngrams)[:200])
#ngrams_frequency = nltk.FreqDist(training_ngrams)
#print(ngrams_frequency.most_common(50))

collocations_list = []
collocations_frequency_list = []
#for w in words_list:
#	training_collocations = myText.collocations()
#	collocations_frequency = nltk.FreqDist(training_collocations)
#	print (training_collocations)
	#collocations_list.extend(training_collocations)
	#collocations_frequency_list.extend(collocations_frequency)


bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(myText, 5)

#finder.apply_freq_filter(50)
scored = finder.score_ngrams(bigram_measures.pmi)
#print (finder.nbest(bigram_measures.likelihood_ratio, 50))
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
	prefix_keys[key[0]].append((key[1], scores))

for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])

my_Dict = { }

for w in words_list:
	prefix_keys_frequency = nltk.FreqDist(prefix_keys)
	#print (w, prefix_keys[w][:10], prefix_keys_frequency.most_common(10), scores) #+ scores
	my_Dict = {w: prefix_keys[w]}
	with codecs.open("./collocations_results", "w", encoding = 'utf-8') as f:
		f.write(str(my_Dict))

#with codecs.open("./collocations_frequency_results", "w", encoding = 'utf-8') as myfile:
#	myfile.write(collocations_frequency_list)
