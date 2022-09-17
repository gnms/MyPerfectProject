
import paho.mqtt.client as mqtt
import socket
import time


client = mqtt.Client("Mats_2")
host_name = socket.gethostname()
IPAddress = socket.gethostbyname(host_name)
print(IPAddress)
for x in range(1, 3):
    try:
        print("try connect {IP}".format(IP=x))
        client.connect("192.168.68.{IP}".format(IP=x))
        print(" connect {IP}".format(IP=x))
    except:
        print("error")
        client = mqtt.Client("Mats_2")


for x in range(0, 10):
    client.publish("house", x)
    time.sleep(3)
