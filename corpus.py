#! /usr/bin/env python
# -*- coding: utf-8 -*-


import nltk
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



#for file in os.listdir('C:/Users/Maximilian Schwenke/brickset-scraper/files'):
	#f = file.open(file, "r")
	#content = f.read()
#tokenized_raw_text = nltk.sent_tokenize(content)
	#tokenized_raw_text = nltk.word_tokenize(content)
	#final_text = str(tokenized_raw_text)
	#print (final_text[0:1000])
file2 = open ("mywords.txt", "r", encoding = "utf-8")
ukrainian_words = file2.read( )
tokenized_file2 = nltk.word_tokenize(ukrainian_words)
word = " "

path = 'C:/Users/Maximilian Schwenke/brickset-scraper/files/'
dirs = os.listdir(path)
for file in dirs:
	f = open(os.path.join(path + file),"r", encoding = 'utf-8')
	content = f.read()
	tokenized_raw_text = nltk.word_tokenize(content)
	final_text = nltk.text.Text(tokenized_raw_text)
	
for word in tokenized_file2:
	concord = final_text.concordance(word)
		
file_output = open ("concordance.txt", "w")
file_output.write(concord)
file_output.close()

#.stdout = tmpout
		
def entropy (words):
	for word in final_text:
		freqdist = nltk.FreqDist(word)
		probs = [freqdist.freq(w) for w in freqdist]
		return -sum(p* math.log (p,2) for p in probs)

def edit_dist_init(len1, len2):
	lev = []
	for i in range (len1):
		lev.append([0]* len2)
	for i in range (len1):
		lev[i][0] = i
	for j in range (len2):
		lev[0][j] = j
	return lev



#file_search = file.open (re.findall *(u'подол')))

#ef concordance(self, word, width=40):
#key = final_search(word)
#wc = int(width/10)                # words of context
#for i in self._index(key):
    #lcontext = ' '.join(self._text[i+wc:i])
    #rcontext = ' '.join(self._text[i:i+wc])
    #ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
    #rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
    #print(ldisplay, rdisplay)
    #final_text.concordance(word)

#ith open ("concordance.txt". 'w') as w:
#concord = concordance(word)
#w.write(concord)

