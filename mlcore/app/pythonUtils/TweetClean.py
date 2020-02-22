import re
import pandas as pd

df = pd.read_csv('data/cyclone.csv')
df.head()
tweets = df['tweet']
result_tweet = []
for tweet in tweets:
    text = tweet
    #removing links
    result = re.sub('http\S+','', text)
    result1 = re.sub('pic\S+','', result)
    #removing #
    result2 = re.sub('#\S+','',result)
    #removing @
    result3 = re.sub('@\S+','',result2)
    #removing emojis
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    word = RE_EMOJI.sub(r'', result3)
    #appending in list
    result_tweet.append(word)
d = {'tweet':result_tweet}
csv_df = pd.DataFrame(d)
csv_df.to_csv('cleaned_data.csv')