import feed_DB
import Ox_DB
import Temp_DB
import send
import log_history

if __name__ == '__main__':
    #db 로그인 정보

    host = (input("host (pi = 175.121.249.37, com = 175.121.249.143) >>"))
    if host == "pi":
        host = '175.121.249.37'
        port = 8138
        db = 'fish_db'

    elif host == "host":
        host = 'localhost'
        port = 3306
        db = 'fish_test'

    else:    
        port = int(input("port (pi는 8138, locla은 3306) >>"))
        db = input("db >>")

    database = str(input("어디에 입력할까요?(먹이, 산소, 온도) >>"))
    #data = int(input("센서값 >>"))
    data_list = list(map(int, input("센서값 >>").split()))
    #db 로그인 정보

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
            


