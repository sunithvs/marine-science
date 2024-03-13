import os
import threading

from django.utils import timezone

import smtplib
import ssl
import threading
from datetime import datetime, timezone, timedelta


from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD



def send_email(message, receiver, subject="Maricon Registration/Login verification"):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = EMAIL_HOST_USER
    receiver_email = receiver
    password = EMAIL_HOST_PASSWORD
    text = message
    message = f'Subject: {subject}\n\n{text}'

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        # utf-8 encoding is used to support special characters
        message = message.encode('utf-8')
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



def get_file_path(instance, filename):
    # Get the current timestamp
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    # Get the file extension
    extension = os.path.splitext(filename)[1]
    # Generate a new filename with the timestamp
    new_filename = f"eventsradar-{timestamp}{extension}"
    return os.path.join("uploads", new_filename)

def sendmail(mail, subject, message):
    threading.Thread(target=send_email, args=(message, mail,subject )).start()
