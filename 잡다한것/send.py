from twilio.rest import Client
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
message = ''

def message_send(text_body, Phone_number):
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
            body = text_body,
            from_='+12183963572',
            to = Phone_number
        )
    print(message.sid)




def money():
    response = urlopen('https://www.twilio.com/console')
    soup = BeautifulSoup(response, 'html.parser' )
    for anchor in soup.find_all('a'):
        print((anchor.get('href', '/')))