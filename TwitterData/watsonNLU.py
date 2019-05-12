import json
import os
import configparser
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson import ApiException
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

class watsonNLUClient():
    def __init__(self):
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.iam_apikey = self.config['IBMWATSON']['iam_apikey']
        self.url = self.config['IBMWATSON']['url']
        self.version = self.config['IBMWATSON']['version']
        
    def getNLUService(self):
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version=self.version,
            iam_apikey=self.iam_apikey,
            url=self.url
        )
        return natural_language_understanding
    
    def sentimentwithWatsonNLU(self,msg):
        try:
            service = self.getNLUService()
            response = service.analyze(
            text=msg,
            features=Features(sentiment=SentimentOptions(document=True))).get_result()
            sentimentLabel = response['sentiment']['document']['label'].upper()
            sentimentScore = response['sentiment']['document']['score']
        except ApiException as ex:
            sentimentLabel = 'NEUTRAL'
            sentimentScore = 0
            print ("Method failed with status code ", str(ex.code), ": ", ex.message)
            pass
        
        return sentimentLabel, sentimentScore
        
        


if __name__ == "__main__":
    watsonNlU = watsonNLUClient()
    msg = '@MThunderslice Making everything about immigration\n\n#XenophobiaOnDisplayMAGA'
    sentimentLabel, sentimentScore = watsonNlU.sentimentwithWatsonNLU(msg)
    
    print(sentimentLabel)
    print(sentimentScore)

