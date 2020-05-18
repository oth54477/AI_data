import Ox_DB_config
from time import sleep
import re
#  main.py
INTERBAL = 2

def Ox(host, port, db, a):
    ## 먹이 통신 값 입력 
    oxygen = [a]
    ##
    #regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = Ox_DB_config.MysqlController(host, port, 'root','kangnam',db)

    while True:
        for result in oxygen:
            mysql_controller.insert_total(result)
            sleep(INTERBAL)
        break