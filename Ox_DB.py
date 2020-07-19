import Ox_DB_config
from time import sleep
import re
#  main.py
INTERBAL = 1

def Ox(host, port, db, avr, tmax, tmin):
    ## 먹이 통신 값 입력 
    avr = [avr]
    tmax = [tmax]
    tmin = [tmin]
    ##
    #regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = Ox_DB_config.MysqlController(host, port, 'root','kangnam',db)

    while True:
        for result in avr:
            mysql_controller.insert_avr(result)
            sleep(INTERBAL)
        for result in tmax:
            mysql_controller.insert_max(result)
            sleep(INTERBAL)
        for result in tmin:
            mysql_controller.insert_min(result)
            sleep(INTERBAL)
        break