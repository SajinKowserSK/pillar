
import requests

URL = 'http://localhost:5000/summarize/'


def test():
    text = "Mrs. Smith states that on Sunday evening (7/14/03) about 20 minutes after sitting down to work at her computer, she developed blurred vision, which she describes as the words on the computer looking fuzzy and seeming to run into each other. When she looked up at the clock on the wall, she had a hard time making out the numbers. At the same time, she also noted a strange sensation in her right eyelid."
    data = {'text': text}
    r = requests.post(url=URL, data=data)
    print(r)
    return r


test()
