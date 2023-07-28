from twilio.rest import Client
import smtplib

TWILIO_SID = "ACa8a867fda28f9c02451a57447d132ef4"
TWILIO_AUTH_TOKEN = "23056fc998a7dd07d6499501222627e4"
TWILIO_VIRTUAL_NUMBER = "+15154747874"
TWILIO_VERIFIED_NUMBER = "+919072622722"
EMAIL = "frenelfabian@gmail.com"
EMAIL_PASSWORD = "hyoqyxngtdclldgm"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=emails, msg=message)
            print("Success")
