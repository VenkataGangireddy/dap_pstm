import tweepy
import datetime
#from datetime import datetime,date,timedelta
import csv
import json


access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "49yh2KepopldjN9rf2a20isGj"
consumer_secret = "Ryz1caenzOTPVod7RVYUOhFS8nMQHWAHw791EF3vtwyd17ChQY"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
sinceDate = datetime.date.today() - datetime.timedelta(1)
untilDate = datetime.date.today()
tweets = []
search_terms = 'Trump'
fetched_tweets = tweepy.Cursor(api.search, q=search_terms, since = sinceDate , until = untilDate, lang='en')
listOfTweets=[]
count = 0
for tweet in fetched_tweets.items(5):
    #listOfTweets.append(tweet._json)
    dict_ = {'User Name': tweet.user.name,
            'id' : tweet.id_str,
            'id_str' : tweet.id_str,
            'Tweet Created At': tweet.created_at,
            'Tweet Text': tweet.text,
            'Retweeted': tweet.retweeted,
            'Phone Type': tweet.source,
            }
    #print(tweet.entities['hashtags'])
    hashtag = ''
    for hashtags in tweet.entities['hashtags']:
        if hashtags != '':
            hashtag = hashtag + '~' + hashtags['text']
    #print(hashtag)
    expandedurl = ''
        
    for urls in tweet.entities['urls']:
        expandedurl = urls['expanded_url']
        #print(urls['expanded_url'])
    
    #print(tweet.metadata['iso_language_code'])
    #if tweet.retweeted == True:
    #print(tweet.user)
    if hasattr(tweet, 'retweeted_status'):
        print(tweet.retweeted_status.user.name)
        
    listOfTweets.append(dict_)
print(count)
    
#print(listOfTweets)