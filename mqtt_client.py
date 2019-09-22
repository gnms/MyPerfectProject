import socket
import logging
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

        self.mqtt_topic.simulation.client.publish(self.client_name)

    def run(self):
        self.setup()
        self.send_message_to_server()
        while True:
            self._log.info('Client {} wait for data'.format(self.client_name))
            data = self.socket.recv(3).decode("utf-8")
            msg_size = int(data)
            data = self.socket.recv(msg_size).decode("utf-8")
            if data:
                mqtt_msg = data.split(':')
                self.notify_client(mqtt_msg[0], mqtt_msg[1])

    def setup(self):
        pass
        # self.subscribe("mats")
        # self.subscribe("per")

    def notify_client(self, topic_str, message):
        topic = self.mqtt_topic.get_message(topic_str)
        if topic != None:
            topic.payload = message
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
