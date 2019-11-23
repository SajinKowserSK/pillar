import boto3
import requests
from flask import jsonify

url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
headers = {
    'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
    'x-rapidapi-key': "f00443165emsh153c5de737def4fp1944f8jsnd6f1569b6c4b",
    'accept': "application/json"
}


aws_access_key_id = 'AKIAJ5DU42PGNQXHXJGA'
aws_secret_access_key = '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'
region = 'us-east-1'

aws_medclient = boto3.client(service_name='comprehendmedical',
                             region_name=region,
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)

aws_compclient = boto3.client(service_name='comprehend',
                              region_name=region,
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)


def summarize(text):
    querystring = {"txt": text, "sentences": "5"}
    summary = requests.request(
        "GET", url, headers=headers, params=querystring).json()['summary']
    medical_info = aws_medclient.detect_entities(Text=text)['Entities']
    sentiment = aws_compclient.detect_sentiment(Text=text, LanguageCode='en')
    entities = aws_compclient.detect_entities(Text=text, LanguageCode='en')
    res = {'medical_info': medical_info, 'summary': summary,
           'sentiment': sentiment, 'entities': entities}
    return jsonify(res)
