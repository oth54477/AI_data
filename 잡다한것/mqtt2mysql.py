import paho.mqtt.client as mqtt
import feed_DB

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#") # Topic /seoul/yuokok을 구독한다.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print(msg.topic)
    print(msg.payload)
    data = str(msg.payload)
    feed_DB.Feed("192.168.0.50", 3306, "fish_db", data)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("175.121.249.37", port= 8137) 
# 외부서버 "175.121.249.37" port 8137, 내부 "192.168.0.50"

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
