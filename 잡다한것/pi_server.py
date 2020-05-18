import feed_DB
import Ox_DB
import Temp_DB
import send
import log_history

def server_con(database, data_list):
 
    host = '175.121.249.37'
    port = 8138
    db = 'fish_db'
 
    for data in data_list:
        if database == "먹이":
            feed_DB.Feed(host, port, db, data)
        elif database == "산소":
            Ox_DB.Ox(host, port, db, data)
        elif database == "온도":
            Temp_DB.Temp(host, port, db, data)
        elif database == "log":
            log_history.show_log()
        else:
            a = feed_DB.Select_Feed(host, port, db)
            print(a)
            text = str(a)
            send.message_send(text,'+821029205447')
            

"""
main파일에서 pi_server.sever.con함수 실행하면 바로 pi mariaDB에 연결해서 테이블에 센서값 입력 or 읽어오거나 or 문자 전송 or 접속 로그 확인하게 만들기
"""