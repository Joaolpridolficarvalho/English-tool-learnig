import smtplib
import email.message
from dotenv import load_dotenv
import os
class SendEmail:
    def __init__(self):
        load_dotenv()


    def send_email(self,message):
        msg = email.message.EmailMessage()
        msg['Subject'] = 'Feedback'
        msg['From'] = os.getenv('EMAIL_FROM')
        msg['To'] = os.getenv('EMAIL_TO')
        password = os.getenv('EMAIL_PASSWORD')
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(message)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(msg['From'], password)
        smtp.send_message(msg)
        