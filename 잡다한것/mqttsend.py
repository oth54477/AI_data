#-*- coding:utf-8 -*-
import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub") #Mqtt Client 오브젝트 생성
mqtt.connect("175.121.249.37", 8137) #MQTT 서버에 연결

mqtt.publish("nodemcu", "led") #토픽과 메세지 발행
mqtt.publish("nodemcu", "led off")

mqtt.loop(2) #timeout 2sec.