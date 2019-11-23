import boto3
import requests

url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
headers = {
    'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
    'x-rapidapi-key': "f00443165emsh153c5de737def4fp1944f8jsnd6f1569b6c4b",
    'accept': "application/json"
    }


aws_access_key_id = 'AKIAJAPO52PFNOEXBA7Q'
aws_secret_access_key ='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'
region = 'us-east-1'

aws_medclient = boto3.client(service_name='comprehendmedical', 
                        region_name=region,
                        aws_access_key_id =  aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key )

aws_compclient = boto3.client(service_name='comprehend', 
                        region_name= region,
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key)


def summarize(text):
    querystring = {"txt": text, "sentences": "5"}
    summary = requests.request("GET", url, headers=headers, params=querystring).json()['summary']
    medical_info = aws_medclient.detect_entities(Text= text)['Entities']
    sentiment = aws_compclient.detect_sentiment(Text= text, LanguageCode='en')
    entities = aws_compclient.detect_entities(Text= text, LanguageCode='en')
    key_pharses = aws_compclient.detect_key_phrases(Text= text, LanguageCode='en')
    res = {'medical_info': medical_info,'summary':summary, 'sentiment': sentiment, 'entities': entities}
    return res

if __name__ == "__main__":
    print(summarize("Mrs. Smith also notes that for the past two to three weeks, "
                    "she has been having intermittent pounding bifrontal headaches "
                    "that worsen with straining, such as when coughing or having a"
                    " bowel movement. The headaches are not positional and are not worse "
                    "at any particular time of day. She rates the pain as 7 or 8 on a "
                    "scale of 1 to 10, with 10 being the worst possible headache. "
                    "The pain lessened somewhat when she took Vicodin that she had "
                    "lying around. She denies associated nausea, vomiting, photophobia, "
                    "loss of vision, seeing flashing lights or zigzag lines, numbness, "
                    "weakness, language difficulties, and gait abnormalities. Her recent "
                    "headaches differ from her “typical migraines,” which have occurred "
                    "about 4-6 times per year since she was a teenager and consist of "
                    "seeing shimmering white stars move horizontally across her vision "
                    "for a couple minutes followed by a pounding headache behind one "
                    "or the other eye, photophobia, phonophobia, and nausea and "
                    "vomiting lasting several hours to two days. She has never "
                    "taken anything for these headaches other than ibuprofen or "
                    "Vicodin, both of which are partially effective. The last "
                    "headache of that type was two months ago."))