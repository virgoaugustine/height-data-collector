import os
from email.mime.text import MIMEText
from smtplib import SMTP

def send_email(username, email, height,avg_height, count):
        #Set my email and address here as environment variables.
    from_email = os.environ.get('GMAIL_ADDRESS') 
    from_password= os.environ.get('GMAIL_PASSWORD')
    to_email = email

    subject = "Height Data"
    message = "Hey there <strong>{}</strong><br> \
             Your height is <strong>{}</strong> and the average height is <strong>{}</strong> \
            calculated out of <strong>{}</strong> people" .format(username, height, avg_height, count)

    msg = MIMEText(message, "html")
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

