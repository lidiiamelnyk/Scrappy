# -*- coding: utf-8 -*-
import codecs

import nltk

content_file = open ("./corpus.txt", "r", encoding ="utf-8")

words_list = []

with codecs.open("./words.txt", "r", encoding="utf-8") as f:
    for line in f:
        words_list.extend(line.split())
print(words_list)
text = content_file.read()

nltk.download('punkt')

tokens = nltk.word_tokenize(text)
print(tokens)
textList = nltk.Text(text)
concord_list = []
for word in words_list:
    conc = textList.concordance(word)
    if conc:
        concord_list.extend(conc)
with codecs.open("./result_file", "w", encoding="utf-8") as f:
    f.write(str(concord_list))
