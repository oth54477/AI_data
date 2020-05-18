import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipse.org")
client.loop_start()

while True:
    temperature = sensor.blocking_read()
    client.publish("paho/temperature", temperature)