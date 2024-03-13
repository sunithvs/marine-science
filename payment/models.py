import smtplib
import ssl
import threading

from django.db import models

from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


# Create your models here.

def generate_id():
    import uuid
    key = uuid.uuid4().hex[:10]
    while True:
        if Payment.objects.filter(id=key).exists():
            key = uuid.uuid4().hex[:10]
        else:
            break
    return key


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


class Payment(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, default=generate_id)
    amount = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    user = models.ForeignKey('auth_login.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default="pending", choices=(("pending", "pending"), ("success", "success"),
                                                                         ("failed", "failed")))
    category = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.id

    def send_email(self):
        msg = (f"New Abstract {self.title}, Submitted  by {self.user.full_name} ({self.user.email})"
               f" on the theme {self.theme} use the link to download the file https://marine.cusat.ac.in{self.file.url}")
        threading.Thread(target=send_email, args=(
            "You have been successfully registered for the participation of MARICON-2024", self.user.email,
            "Maricon abstract submission")).start()
