from flask import Flask
from flask import Flask
from flask import request
import os
import json
import copy
import re
import webutils as wu
from flask import Response
import sys
from operator import itemgetter
import pymysql

sys.path.append("../TwitterData")
from dataServices import dataClient

# Default delimiter to delineate primary key fields in string.
key_delimiter = "_"

data = dataClient()


app = Flask(__name__)

def buildUrl():
    curUrl=request.url
    if curUrl.find("?") > 0:
        newurl=curUrl[:curUrl.find("?")]
    else:
        newurl=curUrl
    st=0
    for k,v in request.args.items():
        if not k == 'offset' and not k == 'limit':
            if st==0:
                newurl+="?"+k+"="+str(v)
                st=1
            else:
                newurl+="&"+k+"="+str(v)
    return newurl


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

            if concept=='all':
                q = "select a.*, twitter_sentiments_tbl.Sentiment_Type as SentimentType, twitter_sentiments_tbl.Sentiment_Percentage as SentimentPercent from (select topic_entities_tbl.Topic_Entity_Id as TopicID, topic_entities_tbl.Entity_Value as TopicName, twitter_data_tbl.Text as TweetMsg, twitter_data_tbl.Tweet_Date as TweetTimestamp, twitter_data_tbl.User_Screen_Name as TweetHandle, twitter_data_tbl.Tweet_Id as TweetID from topic_entities_tbl left join twitter_data_tbl on topic_entities_tbl.Topic_Entity_Id=twitter_data_tbl.Topic_Entity_Id where topic_entities_tbl.Active_Flag=1 AND twitter_data_tbl.Original_Tweet_Id='') as a left join twitter_sentiments_tbl on a.TweetID=twitter_sentiments_tbl.Tweet_Id"
                result = data.run_query(q)
                print(result)

            if result:
                result_data = json.dumps(result, default=str)
                resp = Response(result_data, status=200, mimetype='application/json')
            else:
                resp = Response("Not found", status=404, mimetype="text/plain")

        else:
            return resp

    except Exception as e:
        utils.debug_message("Something awlful happened, e = ", e)

    return resp


if __name__ == '__main__':
    app.run()
