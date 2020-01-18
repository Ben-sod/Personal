#preset values:
accountSID='ACf07592a182cbabd70e427a527e8d690a'
authToken = '1297a995bb7012b1ffc8d41ecfc28fad'
myTwilioNumber = '+17632253531'
myCellPhone = '+17634967518'

from twilio.rest import Client

def textmyself(message):
    twilioCli=Client(accountSID,authToken)
    twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)
