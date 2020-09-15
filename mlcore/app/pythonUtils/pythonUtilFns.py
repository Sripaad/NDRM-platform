import pandas as pd
import csv 
import sys
import spacy 
from spacy.matcher import PhraseMatcher
import re

def locationExtractor():
    
    df = pd.read_csv('datasets/countries.csv', encoding= 'unicode_escape')
    locations = df['Country']
    with open('datasets/locations.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for location in locations:
            writer.writerow([location])
    print("Raw Locations Extracted")

def locationFormatter():
    text = open("dataset/locations.csv","r")
    text = ''.join([i for i in text]).replace('B.O','')
    text = ''.join([i for i in text]).replace(' BO','')
    text = ''.join([i for i in text]).replace(' SO','')
    text = ''.join([i for i in text]).replace(' HO','')
    text = ''.join([i for i in text]).replace('S.O','')
    text = ''.join([i for i in text]).replace('H.O','')
    x = open('datasets/onlylocations.csv',"w")
    x.writelines(text)
    x.close()
    print("Locations Formatted")

def matcherR():
    nlp = spacy.load('en')
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe('ner')
    label = 'GEOLOC'
    matcher = PhraseMatcher(nlp.vocab)
    text = open('onlylocations.csv','r')
    for i in text:
        matcher.add(label, None,nlp(i))
    one = nlp('Chennai has been affected severly beacuse of the tsunami')
    matches = matcher(one)
    [match for match in matches]
    print(matches)

def appendertool():
    df = pd.read_csv('datasets/countries.csv', encoding= 'unicode_escape')
    locations = df['Country']
    df1 = pd.read_csv('onlylocations.csv', encoding= 'unicode_escape')
    df1.append(df, sort=True, ignore_index=True)
    print("countries added to the set")
    
def tsv2csv(): # Useage python3 pythonUtilFns.py <inputFileName.tsv> <outputFileName.csv>
    tabin = csv.reader(sys.stdin, dialect=csv.excel_tab)
    commaout = csv.writer(sys.stdout, dialect=csv.excel)
    for row in tabin:
      commaout.writerow(row)

def preProcessor():
    df = pd.read_csv('datasets/mergedFile.csv', error_bad_lines=False)
    print(df.head())
    tweets = df['tweet']
    result_tweet = []
    for tweet in tweets:
        text = tweet
        #removing links
        result = re.sub('http\S+','', text)
        result1 = re.sub('pic\S+','', result)
        #removing #
        result2 = re.sub('#\S+','',result)
        #removing everything before < 
        result3 = re.sub('^(.* <)',"", result2)
        #removing @
        result4 = re.sub('@\S+','',result3)
        #removing emojis
        RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
        word = RE_EMOJI.sub(r'', result4)
        #appending in list
        result_tweet.append(word)
    d = {'tweet':result_tweet}
    csv_df = pd.DataFrame(d)
    csv_df.to_csv('cleaned_data.csv')
    print("done")
preProcessor()