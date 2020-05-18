# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
"""
문자 한건당 $0.05
body에 문자 내용
to에 전화번호

"""
account_sid = 'AC66cd9d61fd349aee7ddbd351a499012c'
auth_token = 'e177c8002a3afb32a791de87943bac3c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="문자 내용",
         from_='+12183963572',
         to='+821029205447'
     )

print(message.sid)
