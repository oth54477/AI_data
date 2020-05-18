import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import feed_DB
import Ox_DB
import Temp_DB
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

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
    if msg.topic =="/fish_db/ARM":
        GPIO.output(17,True)
        time.sleep(data)
        GPIO.output(17,False)
        GPIO.cleanup()
        # data는 LED 유지 시간
        print("resive data> ", data)

        # 나중에 hostname은 CAT.M1의 IP, port도 CAT.M1으로 바꾸기
        publish.multiple(msgs, hostname="175.121.249.37", port= 8137)
       

# 새로운 클라이언트 생성
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# 외부서버 "175.121.249.37" port 8137, 내부 "192.168.0.50"
client.connect("175.121.249.37", port= 8137) 
client.loop_forever()
