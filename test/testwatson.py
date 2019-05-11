import datetime
#from datetime import datetime,date,timedelta
import csv
import json
from ibm_watson import NaturalLanguageClassifierV1

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='ChZ92fuwi2VyUUqzQ0K9WNzI32Mf4B8wCZu4Q9fSYrry',
    url='https://gateway.watsonplatform.net/natural-language-classifier/api'
)

with open('./weather_data_train.csv', 'rb') as training_data:
    with open('./metadata.json', 'rb') as metadata:
      classifier = natural_language_classifier.create_classifier(
        training_data=training_data,
        metadata=metadata
      ).get_result()
#print(json.dumps(classifier, indent=2))

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-12-19',
    iam_apikey='dnby4_Q9Wx54inSunQ-6xdO2CNIfsVhlatzopCIOsRbR',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api'
)

response = natural_language_understanding.analyze(
    text='@cristinalaila1 @realDonaldTrump Which one of horrific attacks &amp; behavior do you want him to address 1st? He has be\u2026 https://t.co/MnzrkYsWPM',
    features=Features(sentiment=SentimentOptions(document=True))).get_result()


print(response['sentiment']['document']['score'])
print(response['sentiment']['document']['label'])

