import requests
API_KEY = "810cac55-0ba9-4ecc-bf32-fb25d6f342dc"

def summarize(text):
    r = requests.post("https://api.deepai.org/api/summarization",data={'text': text},
        headers={'api-key': API_KEY}

    ).json()

    return r['output']




