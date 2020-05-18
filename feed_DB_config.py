import pymysql
# dbconfig.py
class MysqlController:
    def __init__(self, host, port, id, pw, db_name):
        self.conn = pymysql.connect(host=host, port= port, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_total(self,total):
        sql = 'INSERT INTO 먹이 (먹이_d) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()

    def select(self):
        sql = "SELECT 먹이_p FROM 먹이_pls"
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result

    def delete(self):
        sql = "DELETE FROM 먹이_pls"
        self.curs.execute(sql)
        self.conn.commit()
