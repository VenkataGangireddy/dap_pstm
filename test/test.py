import tweepy
from datetime import datetime,timedelta
import csv
import json


access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "49yh2KepopldjN9rf2a20isGj"
consumer_secret = "Ryz1caenzOTPVod7RVYUOhFS8nMQHWAHw791EF3vtwyd17ChQY"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []
search_terms = 'DIVYA OR IPL'
fetched_tweets = tweepy.Cursor(api.search, q=search_terms, lang='en')
listOfTweets=[]
for tweet in fetched_tweets.items(3):
    #listOfTweets.append(tweet._json)
    dict_ = {'User Name': tweet.user.name,
            'id' : tweet.id_str,
            'id_str' : tweet.id_str,
            'Tweet Created At': tweet.created_at,
            'Tweet Text': tweet.text,
            'Retweeted': tweet.retweeted,
            'Phone Type': tweet.source,
            }
    listOfTweets.append(dict_)
    
print(listOfTweets)