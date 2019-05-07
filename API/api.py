from flask import Flask
from flask import Flask
from flask import request
import json
from flask import Response
import sys

sys.path.append("../TwitterData")
from dataServices import dataClient

# Default delimiter to delineate primary key fields in string.
key_delimiter = "_"

data = dataClient()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
            You probably want to go either to the content home page or call an API at /api.
            When you despair during completing the homework, remember that
            Audentes fortuna iuvat.
            """


@app.route('/api')
def api():
    return 'You probably want to call an API on one of the resources.'


@app.route('/api/get/<concept>', methods=['GET'])
def concept(concept):

    resp = Response("Internal server error", status=500, mimetype="text/plain")

    try:

        if request.method == 'GET':

            #get result here based on concept

            if concept=='tweets':
                q = "select a.*, twitter_sentiments_tbl.Sentiment_Type as SentimentType, twitter_sentiments_tbl.Sentiment_Percentage as SentimentPercent from (select topic_entities_tbl.Topic_Entity_Id as TopicID, topic_entities_tbl.Entity_Value as TopicName, twitter_data_tbl.Text as TweetMsg, twitter_data_tbl.Tweet_Date as TweetTimestamp, twitter_data_tbl.User_Screen_Name as TweetHandle, twitter_data_tbl.Tweet_Id as TweetID from topic_entities_tbl left join twitter_data_tbl on topic_entities_tbl.Topic_Entity_Id=twitter_data_tbl.Topic_Entity_Id where topic_entities_tbl.Active_Flag=1 AND twitter_data_tbl.Original_Tweet_Id='') as a left join twitter_sentiments_tbl on a.TweetID=twitter_sentiments_tbl.Tweet_Id order by TweetTimestamp desc"

                result = data.run_query(q)
                res=[]
                for r in result:
                    res.append({'TopicID':r[0], 'TopicName':r[1], 'TweetMsg':r[2], 'TweetTimestamp':r[3], 'TweetHandle':r[4], 'TweetID':r[5], 'SentimentType':r[6], 'SentimentPercent':r[7]})


            elif concept=='topics':
                q = "select Topic_Entity_Id as TopicID, Entity_Value as TopicName from topic_entities_tbl"

                result = data.run_query(q)
                res={}
                for r in result:
                    res[r[0]]=r[1]


            if result:
                result_data = json.dumps(res, default=str, indent=2)
                resp = Response(result_data, status=200, mimetype='application/json')
            else:
                resp = Response("Not found", status=404, mimetype="text/plain")

        else:
            return resp

    except Exception as e:
        utils.debug_message("Something awlful happened, e = ", e)

    return resp

@app.route('/api/get/trending/<concept>', methods=['GET'])
def trending(concept):

    resp = Response("Internal server error", status=500, mimetype="text/plain")

    try:

        if request.method == 'GET':

            #get result here based on concept
            if request.args.get('limit') is not None:
                setLimit=request.args.get('limit')
            else:
                setLimit=1000

            if concept=='topics':
                q2 = "select Topic_Entity_Id as TopicID, Entity_Value as TopicName from topic_entities_tbl"

                res2 = data.run_query(q2)
                topics={}
                topicsCount={}
                topicPos={}
                topicNeg={}

                for r2 in res2:
                    topics[r2[0]]=r2[1]

                q = "select a.*, twitter_sentiments_tbl.Sentiment_Type as SentimentType, twitter_sentiments_tbl.Sentiment_Percentage as SentimentPercent from (select topic_entities_tbl.Topic_Entity_Id as TopicID, topic_entities_tbl.Entity_Value as TopicName, twitter_data_tbl.Text as TweetMsg, twitter_data_tbl.Tweet_Date as TweetTimestamp, twitter_data_tbl.User_Screen_Name as TweetHandle, twitter_data_tbl.Tweet_Id as TweetID from topic_entities_tbl left join twitter_data_tbl on topic_entities_tbl.Topic_Entity_Id=twitter_data_tbl.Topic_Entity_Id where topic_entities_tbl.Active_Flag=1 AND twitter_data_tbl.Original_Tweet_Id='') as a left join twitter_sentiments_tbl on a.TweetID=twitter_sentiments_tbl.Tweet_Id order by TweetTimestamp desc limit "+str(setLimit)

                result = data.run_query(q)
                tweets={}
                fin={'topics':[]}
                for r in result:
                    if r[0] not in tweets.keys():
                        tweets[r[0]]=[]

                    tweets[r[0]].append({'msg':r[2], 'timestamp':r[3], 'handle':r[4], 'id':r[5], 'sentiment':r[6], 'sentimentPercent':r[7]})

                    if r[0] not in topicsCount.keys():
                        topicsCount[r[0]] = 1
                    else:
                        topicsCount[r[0]]=topicsCount[r[0]]+1

                    if r[6]=='POSITIVE':
                        if r[0] not in topicPos.keys():
                            topicPos[r[0]] = 1
                        else:
                            topicPos[r[0]]=topicPos[r[0]]+1
                    elif r[6]=='NEGATIVE':
                        if r[0] not in topicNeg.keys():
                            topicNeg[r[0]] = 1
                        else:
                            topicNeg[r[0]]=topicNeg[r[0]]+1

                sortedTopics = sorted(topicsCount.items(), key=lambda x:(x[1],x[0]), reverse=True)

                for t in sortedTopics:
                    if t[0] not in topicPos.keys():
                        topicPos[t[0]] = 0
                    if t[0] not in topicNeg.keys():
                        topicNeg[t[0]] = 0

                    fin['topics'].append({'id':t[0],
                                'name':topics[t[0]],
                                'count':topicsCount[t[0]],
                                'positive':topicPos[t[0]],
                                'negative':topicNeg[t[0]],
                                'tweets':tweets[t[0]]})


            if result:
                result_data = json.dumps(fin, default=str, indent=2)
                resp = Response(result_data, status=200, mimetype='application/json')
            else:
                resp = Response("Not found", status=404, mimetype="text/plain")

        else:
            return resp

    except Exception as e:
        utils.debug_message("Something awlful happened, e = ", e)

    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
