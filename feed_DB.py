import feed_DB_config
from time import sleep
import re
#  main.py
INTERBAL = 2

def Feed(host, port, db, a):
    ## 먹이 통신 값 입력 
    feed = [a]
    ##
    #regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)

    while True:
        for result in feed:
            mysql_controller.insert_total(result)
            sleep(INTERBAL)
        break

def Select_Feed(host,port,db):
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    result = mysql_controller.select()
    return result

def Delete_Feed(host,port,db):
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    mysql_controller.delete()