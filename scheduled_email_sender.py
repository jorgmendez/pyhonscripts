import smtplib
from email.mime.text import MIMEText
import time

def send_email(email, password, recipient, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = email

    # Setup the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the email server
    server.login(email, password)

    # Send the email
    server.send_message(msg)

    # End the SMTP session
    server.quit()

email = "youremail@example.com"
password = "yourpassword"
recipient = "recipientemail@example.com"
subject = "Scheduled Email"
message = "This is a scheduled email sent using Python."

# Schedule the email to be sent at a specific time
send_time = time.mktime(time.strptime("2023-02-05 13:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
if current_time < send_time:
    time.sleep(send_time - current_time)

send_email(email, password, recipient, subject, message)
