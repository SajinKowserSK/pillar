
import requests

account_sid = "AC777c3e32c331cf18084b4a08be67e188"
auth_token = "e4a2a1ebe6aa4d9ebd66cc3bac87d8fb"
base = "https://" + account_sid + ":" + auth_token + \
    "@api.zang.io/v2/Accounts/" + account_sid
SMS_URL = base+"/SMS/Messages.json"
CALL_URL = base+"/Calls.json"


def sendText(message, number):
    data = {"From": "+1 647-930-8813", "To": number, "Body": message}
    r = requests.post(url=SMS_URL, data=data)
    return r


def makeCall(number):
    data = {"From": "+1 647-930-8813", "To": number,
            "Url": "http://cloud.zang.io/data/inboundxml/34b244e3a9bba1a1e2e8bb65d0c549fd2e1bb1ca"
            }
    r = requests.post(url=CALL_URL, data=data)
    return r


if __name__ == "__main__":
    sendText("Hi, Shafin.", "416-880-9456")
