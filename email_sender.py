import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sender_name'
email['to'] = 'email_you_are_sending_to'
email['subject'] = 'You won 1,000,000 dollars!'


email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	#tls is an encryption mechanism
	smtp.starttls()
	smtp.login('email_you_are_sending_from', 'password_email')
	smtp.send_message(email)
	print('All good')