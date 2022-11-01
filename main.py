from subprocess import Popen, PIPE, STDOUT
from event import Event
import json
import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv()

SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SUBJECT = 'PET Virtual Machine Services'

def send_email(body):
    msg = email.message.Message()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    password = APP_PASSWORD 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email enviado para {RECEIVER}')

def dispatcher(event_json):
    event = Event(event_json)
    print(event.name())
    print(event.logs())
    print("\n\n")

def main():
    docker_events = "docker events --filter event=die --format '{{json .}}'"
    process = Popen(docker_events, shell=True, stdout=PIPE, stderr=STDOUT)

    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            json_string = line.decode("utf-8").strip()
            dispatcher(json.loads(json_string))

if __name__ == "__main__":
    main()
