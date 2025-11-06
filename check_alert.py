import os, sys, smtplib, ssl
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta

THINGSPEAK_CHANNEL_ID = "3150721"
THINGSPEAK_READ_KEY = "UK3SJS47MXQ82PAD"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME =pushpalathamusunuru9@gmail.com
SMTP_PASSWORD = "ntcw fjcu eyjt qhlq"
FROM_EMAIL = "pushpalathamusunuru9@gmail.com"
TO_EMAIL = "pushpalathamusunuru9@gmail.com"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

def main():
    url = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/fields/1.json?api_key={THINGSPEAK_READ_KEY}&results=1"
    r = requests.get(url)
    data = r.json()

    field1 = data["feeds"][0]["field1"]
    created_at = data["feeds"][0]["created_at"]

    if field1 == "1":
        subject = "🚨 Sound Alert Detected!"
        body = f"High-risk sound detected at (UTC): {created_at}"
        send_email(subject, body)
        print("Email Sent ✅")
    else:
        print("No alert.")

if __name__ == "__main__":
    main()
