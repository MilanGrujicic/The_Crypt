import json
import os
from twilio.rest import Client

with open('numbers.json') as f:
    winning_numbers = json.load(f)

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_number = "+12514188679"
my_number = "+38669785000"
played_numbers = [1, 3, 25, 27, 34, 11, 12]  # Replace with actual played numbers

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=twilio_number,
    body=f"Winning Numbers: {winning_numbers}\nPlayed Numbers: {played_numbers}",
    to=my_number
)

os.remove('numbers.json')