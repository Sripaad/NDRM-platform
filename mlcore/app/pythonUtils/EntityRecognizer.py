import spacy 
from spacy.matcher import PhraseMatcher
import plac
from pathlib import Path
import random


'''
Below Function converts the output of the PhraseMatcher to something useable in training.
The Training data needs a string index of characters(start, end, label) while the matched output
uses index of words from a NLP document.
'''
def offseter(lbl, doc, matchitem):
    o_one = len(str(doc[0:matchitem[1]]))
    subdoc = doc[matchitem[1]:matchitem[2]]
    o_two = o_one + len(str(subdoc))
    return(o_one,o_two,lbl)

'''
Here we load SpaCy and setup the pipes for training.
'''
nlp = spacy.load('en')
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner)
else:
    ner = nlp.get_pipe('ner')
    
'''
This is to make our lives easier.
Here we're using the PhraseMatcher class from SpaCy to locate the text we want to label.
'''
label = 'GEOLOC'
matcher = PhraseMatcher(nlp.vocab)
text = open('datasets/onlylocations.csv','r')
for i in text:
    matcher.add(label, None,nlp(i))
one = nlp('Chennai has been affected severly beacuse of the tsunami')
matches = matcher(one)
[match for match in matches]

'''
Gathering Training Data.
Here the dataset contains tweets from the 2015_Nepal_Earthquake (taken from 
https://crisisnlp.qcri.org/, originally a '.tsv' file it has been converted '.txt'. 
'''
res = []
to_train_ents = []
with open('datasets/sampleData.txt') as gh:
    line = True
    while line:
        line = gh.readline()
        mnlp_line = nlp(line)
        matches = matcher(mnlp_line)
        res = [offseter(label, mnlp_line, x)for x in matches]
        to_train_ents.append((line, dict(entities=res)))
        
'''
Actually Train the Recognizer.
'''
optimizer = nlp.begin_training()
other_pipes = [pipe for pipe in nlp.pipe_names if pipe !='ner']

with nlp.disable_pipes(*other_pipes):   # only train NER
    for itn in range(20):
        losses = {}
        random.shuffle(to_train_ents)
        for item in to_train_ents:
            nlp.update([item[0]], [item[1]], sgd = optimizer, drop = 0.35, losses = losses)
        