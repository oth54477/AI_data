import dbconfig
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
#  main.py
url = 'https://www.ethernodes.org/network/1'
INTERBAL = 60
if __name__=='__main__':
    regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = dbconfig.MysqlController('localhost','root','kangnam','entire_nodes')

    while True:
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            items = soup.find_all('li')

            for item in items:
                result = regex.search(item.text)
                if result:
                    mysql_controller.insert_total(result.groups(1)[0])
                    a = type(result)
                    print(a)
                    sleep(INTERBAL)