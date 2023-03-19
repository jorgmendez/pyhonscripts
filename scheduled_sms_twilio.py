from twilio.rest import Client
import time

def send_sms(account_sid, auth_token, from_number, to_number, message):
    client = Client(account_sid, auth_token)

    #SMS message
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=message
    )

# Define the Twilio account information and SMS details
account_sid = "your_account_sid"
auth_token = "your_auth_token"
from_number = "number given fromt twilio"
to_number = "desired number"
message = "This is a scheduled SMS sent using Python and Twilio."

# Schedule the SMS to be sent at a specific time
send_time = time.mktime(time.strptime("2023-02-05 13:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
if current_time < send_time:
    # If the current time is before the send time, sleep until the send time
    time.sleep(send_time - current_time)

# Send the SMS
send_sms(account_sid, auth_token, from_number, to_number, message)
