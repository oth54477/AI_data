import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import feed_DB
import Ox_DB
import Temp_DB


"""
토픽이 아닌 / 로 구분 (ex : 온도값/산소값/먹이값)
처음 1회 실행시 arm 에서 데이터 받으면 회신 해서 접속 연결 확인
서버 데이터를 AI에서 읽어올 수 있도록 작성

"""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)
    # 모든 Topic을 구독한다.
    client.subscribe("#") 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #DB접속 정보
    host = "192.168.0.50"
    port = 3306
    db = "fish_db"
    
    #받은 데이터 형식에서 데이터값만 분류
    Strdata = str(msg.payload)
    data = Strdata.strip("b'")
    print(msg.topic+"\n"+data)
    data = int(data)
    
    
    #topic에 따라서 분류 후 DB로 전송
    if msg.topic =="/fish_db/Feed":
        feed_DB.Feed(host, 3306, db, data)
        print("Successful transfer to server. > Feed ", data)
    elif msg.topic == "/fish_db/Oxygen":
        Ox_DB.Ox(host, 3306, db, data)
        print("Successful transfer to server. > Ox", data)
    elif msg.topic == "/fish_db/Temp":
        Temp_DB.Temp(host, 3306, db, data)
        print("Successful transfer to server. > Temp", data)
    #request 토픽 수신시 DB값 ARM으로 전송
    elif msg.topic == "/fish_db/request":
        re = feed_DB.Select_Feed(host,port,db)
        re = str(re)
        r = re.strip("((,),)")
        r = int(float(r))
        
        print(re)
        msgs = \
        [
            {
                'topic':"/fish_db/ARM",
                'payload':r
            },
        ]
        # 나중에 hostname은 CAT.M1의 IP, port도 CAT.M1으로 바꾸기
        publish.multiple(msgs, hostname="175.121.249.37", port= 8137)
        feed_DB.Delete_Feed(host, 3306, db)
        
        print("Successful transfer to server. > ARM", )

# 새로운 클라이언트 생성
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# 외부서버 "175.121.249.37" port 8137, 내부 "192.168.0.50"
client.connect("175.121.249.37", port= 8137) 
client.loop_forever()
