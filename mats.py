
import imp
import paho.mqtt.client as mqtt
import socket
import time


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


client = mqtt.Client("Mats")
host_name = socket.gethostname()
IPAddress = socket.gethostbyname(host_name)
client.connect(IPAddress)


client.on_message = on_message  # attach function to callback
client.subscribe("house")
client.loop_start()  # start the loop
time.sleep(40)  # wait
client.loop_stop()  # stop the loop
