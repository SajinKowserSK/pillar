import requests
from aylienapiclient import textapi
import boto3

aws_access_key_id = 'AKIAJAPO52PFNOEXBA7Q'
aws_secret_access_key ='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'
region = 'us-east-1'

summaryclient = textapi.Client("92fce724", "1ec12ed404cd44234d65fcc666c63f1e")

aws_medclient = boto3.client(service_name='comprehendmedical', 
                        region_name=region,
                        aws_access_key_id =  aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key )

aws_compclient = boto3.client(service_name='comprehend', 
                        region_name= region,
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key)
def summarize(text):
    summary = summaryclient.Summarize({'text': text.encode('utf-8'), 'title': "Medical, Disease, Illness", 'sentences_percentage': 50})
    medical_info = aws_medclient.detect_entities(Text= text)['Entities']
    sentiment = aws_compclient.detect_sentiment(Text= text, LanguageCode='en')
    entities = aws_compclient.detect_entities(Text= text, LanguageCode='en')
    key_pharses = aws_compclient.detect_key_phrases(Text= text, LanguageCode='en')
    res = {'medical_info': medical_info, 'summary': summary, 'sentiment': sentiment, 'entities': entities}
    return res