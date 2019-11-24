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


def summarize(text, db):
    querystring = {"txt": text, "sentences": "5"}
    summary = requests.request(
        "GET", url, headers=headers, params=querystring).json()['summary']
    med_entities = aws_medclient.detect_entities(Text=text)['Entities']
    med_info = [{'Category': x['Category'], 'Text': x['Text'],
                 'Traits': x['Traits'], 'Type': x['Type']} for x in med_entities]
    sentiment = aws_compclient.detect_sentiment(
        Text=text, LanguageCode='en')['Sentiment']
    entities = [x['Text'] for x in aws_compclient.detect_entities(
        Text=text, LanguageCode='en')['Entities']]
    res = {'medical_info': med_info, 'summary': summary,
           'sentiment': sentiment, 'entities': entities}
    if db:
        return res

    return jsonify(res)