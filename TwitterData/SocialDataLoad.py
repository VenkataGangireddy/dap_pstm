from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
import tornado.gen
import time
from tweetData import TwitterClient

@tornado.gen.coroutine
def load_data():
    yield tornado.gen.sleep(300)
    loadData()
    raise tornado.gen.Return(True)


class LoadTweetData(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        loadCompleted = load_data()
        self.write('Tweet Data load completed'.format(loadCompleted))
        self.finish()

def loadData():

	# creating object of TwitterClient and dataClient Class
	api = TwitterClient()
	data = dataClient()

	#Read topics from database

	results = data.read_topics()

	for topic in results:
		Topic_Entity_Id = topic[2]
		Topic_Entity_Value = topic[4]
		# calling function to get tweets
		tweets = api.get_tweets(topic_Entity_id=Topic_Entity_Id,query = Topic_Entity_Value, count = 200)
		# print (tweets)
		tweetsDF = pd.DataFrame(tweets)
		tweetsDFCopy = tweetsDF.copy
		twitterDataDF = tweetsDF.drop(['Sentiment_Type','Sentiment_Percentage'],axis=1)

		data.saveDatatoDB(twitterDataDF,'twitter_data_tbl')
		sentimentDataDF = tweetsDF[['Tweet_Id','Topic_Entity_Id','Sentiment_Type','Sentiment_Percentage','Created_Date','Modified_Date']]
		data.saveDatatoDB(sentimentDataDF,'twitter_sentiments_tbl')

		

if __name__ == "__main__":
    handler_mapping = [
                       (r'/loadTweetData', LoadTweetData),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()

