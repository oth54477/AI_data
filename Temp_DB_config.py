import pymysql
# dbconfig.py
class MysqlController:
    def __init__(self, host, port, id, pw, db_name):
        self.conn = pymysql.connect(host=host, port= port, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_avr(self,total):
        sql = 'INSERT INTO Temp (Temp_avr) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()

    def insert_max(self,total):
        sql = 'INSERT INTO Temp (Temp_max) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()

    def insert_min(self,total):
        sql = 'INSERT INTO Temp (Temp_min) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()