# -*- coding: utf-8 -*-

import nltk

from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re

paragraph = "Dem Input Text"


# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    
    
# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)

words = model.wv.vocab

# Finding Word Vectors
vector = model.wv['war']

# Most similar words
similar = model.wv.most_similar('Similar Word Input')