from twilio.rest import Client
from datetime import datetime
import time

account_sid = 'REGENERATE_THIS'
auth_token = 'REGENERATE_THIS'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent! SID: {message.sid}')
    except Exception as e:
        print("Twilio Error:", e) 


name = input('Enter the recipient name = ')
recipient_number = input('Enter Whatsapp number with country code (e.g +91...): ')
message_body = input(f'Enter the message to {name}: ')

date_str = input('Enter date (YYYY-MM-DD): ')
time_str = input('Enter time (HH:MM 24hr): ')

schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

delay_seconds = (schedule_datetime - current_datetime).total_seconds()

if delay_seconds <= 0:
    print(" Error: Given time is in the past!")
else:
    print(f"Message scheduled at {schedule_datetime}")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
