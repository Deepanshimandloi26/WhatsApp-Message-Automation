"""
twilio
datetime
1- twilio client setup
2- user inputs
3- scheduling logic
4- send message
"""

from twilio.rest import Client
from datetime import datetime. timedelta
import time

account_sid = 'AC25578bfc374c5d39c593341ba14bbe9e'
auth_token = '35b2db49e61811b4ec7828998fa4010b'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body)
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886'
            body=message_body
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g, +91))
message_body = input(f'enter the message you want to {name}: ')

date-str = input('enter the date to send the message (YYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24hour format): ')

