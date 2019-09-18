import socket
import logging


class mqtt_client():
    def __init__(self, host, port, client_name):
        self.host = host
        self.port = port
        self.client_name = client_name

        self._log = logging.getLogger('my_perfect_project')
        self._log.setLevel(logging.DEBUG)
        fh = logging.FileHandler('my_perfect_project.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s :: mqtt_client :: %(levelname)s :: %(funcName)s(%(lineno)d) :: %(message)s')
        fh.setFormatter(formatter)
        self._log.addHandler(fh)
        self._log.info('Started')

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def run(self):
        while True:
            self._log.info('Client {} wait for data'.format(self.client_name))
            data = self.socket.recv(3).decode("utf-8")
            self._log.info('Msg size = {} Client {}'.format(
                data, self.client_name))
            msg_size = int(data)
            data = self.socket.recv(msg_size).decode("utf-8")
            self._log.info('Msg = {} Client {}'.format(
                data, self.client_name))
            if data:
                mqtt_msg = data.split(':')
                self.handel_messages(mqtt_msg[0], mqtt_msg[1])

    def setup(self):
        self.socket.sendall(b'014subscribe:mats')
        self.socket.sendall(b'013subscribe:per')

    def handel_messages(self, topic, message):
        self._log.info('Client {} got topic = "{}" message = "{}"'.format(
            self.client_name, topic, message))

    def send_message(self, topic, message):
        pass


if __name__ == "__main__":
    client = mqtt_client('', 12345, "kalle")
    client.setup()
    client.run()
