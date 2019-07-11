import tweepy
import csv
import pandas as pd

def percentage(part, whole):
    return 100 * float(part)/float(whole)


CONSUMER_KEY = "67FIvkR2aJzeJmPaOfjF2gt23"

CONSUMER_SECRET = "ajtf6jPYfsVvMLQ9gt2zQ1FKIwTJr8bhdmRcCwXu0iTk02LSFx"

ACCESS_TOKEN = "296957600-fFNGCmipPdrvrLtKbiN2vD5i7445nl5BmNynJAwp"

ACCESS_SECRET = "hF1sQdGYwJiGZapH2CwKFUIRhR7wNsjbrVpfQ3ENGNUE4"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)
# ---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends.
# This is the equivalent of /timeline/home on the Web.
# ---------------------------------------------------------------------------------------------------------------------

csvFile = open('data.csv', 'a', encoding='utf-16')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q= "الصيف", lang="ar").items(5):
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-16')])

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('Arabic'))
#file1 = open("data.csv")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filtereddata.csv','a')
        appendFile.write(" "+r)
        appendFile.close()