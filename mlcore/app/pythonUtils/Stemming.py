# -*- coding: utf-8 -*-

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = "Dem Input Text"
               
               
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)   
    
    
    
    
    
    
    
    
    