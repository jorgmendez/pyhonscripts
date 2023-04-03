
from twilio.rest import Client

# Define your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'


to_number = '+1234567890' 
from_number = '+0987654321' 


client = Client(account_sid, auth_token)


message = client.messages.create(
    body='Hello, this is a test SMS from Twilio!', 
    from_=from_number,
    to=to_number
)


print('SMS sent! Message ID:', message.sid)
