import pymysql
# dbconfig.py
class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_total(self,total):
        sql = 'INSERT INTO try (number) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()