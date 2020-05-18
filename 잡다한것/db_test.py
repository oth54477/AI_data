import dbNumber
from time import sleep
import re
#  main.py
INTERBAL = 15
Number1 = [1,2,3]
if __name__=='__main__':
    regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = dbNumber.MysqlController('localhost','root','kangnam','try')

    while True:
        for result in Number1:
            mysql_controller.insert_total(result)
            sleep(INTERBAL)
        break