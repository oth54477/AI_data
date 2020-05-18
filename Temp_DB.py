import Temp_DB_config
from time import sleep
import re
#  main.py
INTERBAL = 2

def Temp(host,port, db, a):
    ## 먹이 통신 값 입력 
    temp = [a]
    ##
    #regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = Temp_DB_config.MysqlController(host, port, 'root','kangnam',db)

    while True:
        for result in temp:
            mysql_controller.insert_total(result)
            sleep(INTERBAL)
        break