from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
"""
response = urlopen('https://www.twilio.com/console')
soup = BeautifulSoup(response, 'html.parser' )
for anchor in soup.select(span.ui-component-tooltip__anchor):
    print((anchor.get_text()))

"""
try:
    response = urlopen('https://www.mangoplate.com/search/%ED%95%98%EB%82%A8%EC%8B%9C')
    soup = BeautifulSoup(response, 'html.parser' )
    for anchor in soup.select('h2.title'):
        print((anchor.get_text()))

except HTTPError as e:

    print(e)

       