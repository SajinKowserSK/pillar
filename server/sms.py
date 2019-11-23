from twilio.rest import Client
account_sid = 'AC3c5103ca2e38659707d0361aa8c824de'
auth_token = 'c9ec3ddeb48b2d5af44cf40f280b27ca'
client = Client(account_sid, auth_token)

def sendText(message, number):
    client.messages.create(body=message,from_='+12316689901',to=number)

if __name__ == "__main__":
    sendText("Hi, Shafin.","+16478918425")



