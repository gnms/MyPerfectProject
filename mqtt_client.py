import socket
import logging
import sys
from mqtt_topic import mqtt_topic_ifd


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

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

        self.mqtt_topic = mqtt_topic_ifd()

        self.mqtt_topic.simulation.connected.publish(self.client_name)

        self.calback_dictonary = dict()

        self.subscribe_with_method_name = True

    def run(self):
        self.mqtt_topic.environment.date_time.subscribe()
        self.mqtt_topic.simulation.verbose.subscribe()
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
                # Method exists and was used.
                except AttributeError:
                    pass
        self.send_message_to_server()
        while True:
            # self._log.info('Client {} wait for data'.format(self.client_name))
            size_in_header = self.socket.recv(3).decode("utf-8")
            msg_size = int(size_in_header)
            # data = self.socket.recv(msg_size).decode("utf-8")
            read_data = 0
            data = ""
            while read_data < msg_size:
                data = data + \
                    self.socket.recv(msg_size-read_data).decode("utf-8")
                read_data = len(data)
                if read_data < msg_size:
                    self._log.info('Client {} MOREEEEEE'.format(
                        self.client_name))
            if data:
                delimiter_pos = data.find(':')
                topic = data[:delimiter_pos]
                pyaload = data[delimiter_pos+1:]
                if self.mqtt_topic.simulation.verbose == topic:
                    self.mqtt_topic.simulation.connected.publish(
                        self.client_name)
                    self.send_message_to_server()
                else:
                    self.notify_client(topic, pyaload)

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

            if self.mqtt_topic.environment.date_time == topic:
                self.mqtt_topic.simulation.idle.publish(self.client_name)

            # time to send all data
            self.send_message_to_server()

    def send_message_to_server(self):
        message_to_send = self.mqtt_topic.get_message_to_send()
        for msg in message_to_send:
            self.send_on_socket(msg)
        self.mqtt_topic.clear_message_to_send()

    def handel_messages(self, topic):
        pass

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
