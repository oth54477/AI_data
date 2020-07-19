import feed_DB_config
from time import sleep
import re
#  main.py
INTERBAL = 0.5

def Feed(host, port, db, avr, tmax, tmin):
    ## 먹이 통신 값 입력 
    ##
    avr = [avr]
    tmax = [tmax]
    tmin = [tmin]
    #regex = re.compile(r'Total(.*\d)\s')
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    
    
    mysql_controller.insert(avr,tmax,tmin)
    sleep(INTERBAL)

def Select_Feed(host,port,db):
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    result = mysql_controller.select()
    return result
def AI_Feed(host,port,db):
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    avr = mysql_controller.AI_feed_avr()
    min = mysql_controller.AI_feed_min()
    max = mysql_controller.AI_feed_max()
    return avr,min,max

def Delete_Feed(host,port,db):
    mysql_controller = feed_DB_config.MysqlController(host, port, 'root','kangnam',db)
    mysql_controller.delete()
