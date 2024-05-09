from mqtt_topic import mqtt_topic_ifd
import sys
import logging
import socket
import time
import re
if __debug__ != True:
    import paho.mqtt.client as mqtt


class mqtt_client():
    def __init__(self, client_name):
        self.host = ''
        self.port = 12345
        self.client_name = client_name

        self._log = logging.getLogger('my_perfect_project')
        self._log.setLevel(logging.DEBUG)
        fh = logging.FileHandler('my_perfect_project.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s :: '+self.client_name+' :: %(levelname)s :: %(funcName)s(%(lineno)d) :: %(message)s')
        fh.setFormatter(formatter)
        self._log.addHandler(fh)
        self._log.info('Started')
        self.not_connected = False
        # Connect to own mqtt server or a real one
        if __debug__ == True:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            # connected
            self.not_connected = True
        else:
            self.mqqt_client = mqtt.Client(client_name)
            mqtt_connected = False
            while mqtt_connected == False:
                try:
                    self.mqqt_client.connect("127.0.0.1")
                    mqtt_connected = True
                except:
                    time.sleep(1)
                    pass

            self.mqqt_client.on_connect = lambda client, userdata, flags, rc: self.on_connect(
                client, userdata, flags, rc)
            self.mqqt_client.on_message = lambda client, userdata, msg: self.on_message(
                client, userdata, msg)

        self.mqtt_topic = mqtt_topic_ifd()

        # not send that we have connected if we not simulate
        if __debug__ == True:
            self.mqtt_topic.simulation.connected.publish(self.client_name)

        self.calback_dictonary = dict()

        self.subscribe_with_method_name = True

        ## Regex to validate the incoming data, teh data shall always start with 3 digits that is the size of the message
        self.validate_size = re.compile("^[0-9]{3}$")

    def run(self):
        # we do not have to subscribe for verbose or time

        if __debug__ == True:
            self.mqtt_topic.environment.date_time.subscribe()
            self.mqtt_topic.simulation.verbose.subscribe()
        else:
            # have to wait for be connected to broaker
            while (self.not_connected):
                time.sleep(1)
        self.setup()
        if self.subscribe_with_method_name:
            for name in self.mqtt_topic.message_dictonary:
                try:
                    method_name = name.replace("/", "_")
                    if hasattr(self, method_name):
                        callback = getattr(self, method_name)
                        if callable(callback):
                            self.mqtt_topic.message_dictonary[name].subscribe()
                            self.calback_dictonary[name] = callback
                            if __debug__ != True:
                                self.mqqt_client.subscribe(name)
                # Method exists and was used.
                except AttributeError:
                    pass
        if __debug__ == True:
            self.send_message_to_server()
            while True:
                # self._log.info('Client {} wait for data'.format(self.client_name))
                size_in_header = self.socket.recv(3).decode("utf-8")

                if self.validate_size.match(size_in_header):
                    msg_size = int(size_in_header)
                    # data = self.socket.recv(msg_size).decode("utf-8")
                    read_data = 0
                    data = ""
                    while read_data < msg_size:
                        data = data + \
                            self.socket.recv(msg_size-read_data).decode("utf-8")
                        read_data = len(data.encode())
                        if read_data < msg_size:
                            self._log.info('Client {} MOREEEEEE'.format(
                                self.client_name))
                    if data:
                        result = re.search(
                            r"(^[^:]{1,}):([^:]{0,}):(.{0,}$)", data)
                        groups = result.groups()
                        topic = groups[0]
                        pyaload = groups[2]
                        if self.mqtt_topic.simulation.verbose == topic:
                            self.mqtt_topic.simulation.connected.publish(
                                self.client_name)
                            self.send_message_to_server()
                        else:
                            self.notify_client(topic, pyaload)
                else:
                    self._log.info('Client {} not correct size'.format(
                                self.client_name))
        else:
            self.mqqt_client.loop_start()  # start the loop
            while True:
                a = 0
            self.mqqt_client.loop_stop()  # stop the loop

    def setup(self):
        pass

    def notify_client(self, topic_str, message):
        topic = self.mqtt_topic.get_message(topic_str)
        if topic != None:
            topic.payload = message

            if self.subscribe_with_method_name:
                if topic_str in self.calback_dictonary:
                    payload_to_msg = None
                    try:
                        payload_to_msg = topic.get_payload()
                        self.calback_dictonary[topic_str](payload_to_msg)
                    except:
                        self.calback_dictonary[topic_str]()
            else:
                self.handel_messages(topic)
            if __debug__ == True:
                if self.mqtt_topic.environment.date_time == topic:
                    self.mqtt_topic.simulation.idle.publish(self.client_name)

            # time to send all data
            self.send_message_to_server()

    def send_message_to_server(self):
        message_to_send = self.mqtt_topic.get_message_to_send()
        for msg in message_to_send:
            if __debug__ == True:

                self._log.info('Send {} new data'.format(msg))
                self.send_on_socket(msg)
            else:
                # we have to parse out if we have some flags that we shall send to mqtt
                result = re.search(r"(^[^:]{1,}):([^:]{0,}):(.{1,}$)", msg)
                groups = result.groups()
                # if we shall send retain
                if groups[0]:
                    self.mqqt_client.publish(
                        groups[0], groups[2], qos=0, retain=True)
                else:
                    self.mqqt_client.publish(groups[0], groups[2])

        self.mqtt_topic.clear_message_to_send()

    def handel_messages(self, topic):
        pass

    # mqtt callback on new messages

    def on_connect(self, client, message, flags, rc):
        self.not_connected = True

    def on_message(self, client, userdata, message):
        self.notify_client(message.topic, str(message.payload.decode("utf-8")))

    # def publish(self, topic):
    #     message = topic.payload
    #     self.send_on_socket(self.create_message(topic, message))

    # def subscribe(self, topic):
    #     if isinstance(topic, str):
    #         topic_str = topic
    #     else:
    #         topic_str = topic.topic

    #     self.send_on_socket(self.create_message("subscribe", topic_str))

    # def create_message(self, topic, message):
    #     if isinstance(topic, str):
    #         topic_str = topic
    #     else:
    #         topic_str = topic.topic

    #     message_to_send = '{}:{}'.format(topic_str, message)
    #     message_to_send = str(len(message_to_send)).rjust(
    #         3, '0') + message_to_send

    #     return message_to_send

    def send_on_socket(self, message):
        self.socket.sendall(message.encode())


if __name__ == "__main__":
    client = mqtt_client("kalle")
    # client.setup()
    client.run()
