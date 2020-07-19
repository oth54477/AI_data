import pymysql
# dbconfig.py
class MysqlController:
    def __init__(self, host, port, id, pw, db_name):
        self.conn = pymysql.connect(host=host, port= port, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert(self,t1,t2,t3):
        sql = 'INSERT INTO Feed (feed_avr, feed_max, feed_min) VALUES (%s, %s, %s)'
        self.curs.execute(sql,(t1,t2,t3,))
        self.conn.commit()

"""
    def select(self,host,port,db,sql):
        mysql_controller = MysqlController(host, port, 'root','kangnam',db)
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result
"""

    def select(self):
        sql = "SELECT feed_p FROM Feed_pls"
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result

    def AI_feed_avr(self):
        sql = "SELECT feed_avr FROM Feed"
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result

    def AI_feed_max(self):
        sql = "SELECT feed_max FROM Feed"
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result

    def AI_feed_min(self):
        sql = "SELECT feed_min FROM Feed"
        self.curs.execute(sql)
        self.conn.commit()
        result = self.curs.fetchall()
        return result

    def delete(self):
        sql = "DELETE FROM Feed_pls"
        self.curs.execute(sql)
        self.conn.commit()
