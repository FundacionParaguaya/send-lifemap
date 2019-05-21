from secrets import SID, AUTH, OWN_NUMBER
from twilio.rest import Client

SMS_NUMBER = "+5521933007184"
WHATS_NUMBER = "whatsapp:+14155238886"

PDF = "https://informacionpublica.paraguay.gov.py/public/ley_5282.pdf"
BEST_IMG = "http://www.dumpaday.com/wp-content/uploads/2018/09/photos-21-3.jpg"
RANDOM_IMG = "https://picsum.photos/640/480"

client = Client(SID, AUTH)

message = client.messages.create(
    from_=WHATS_NUMBER,
    media_url=RANDOM_IMG, #You can test it with PDF also    
    body="This is a test of Twilio's Whastapp API using the PovertyStoplight stuff",
    to="whatsapp:" + OWN_NUMBER, 
)

print(message.sid)