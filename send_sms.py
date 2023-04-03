
from twilio.rest import Client

# Define your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Define the phone number to send the SMS to and your Twilio phone number
to_number = '+1234567890' # Replace with the phone number you want to send the SMS to
from_number = '+0987654321' 


client = Client(account_sid, auth_token)


message = client.messages.create(
    body='Hello, this is a test SMS from Twilio!', 
    from_=from_number,
    to=to_number
)


print('SMS sent! Message ID:', message.sid)
