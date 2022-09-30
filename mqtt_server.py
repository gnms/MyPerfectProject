import threading
import socket
from mqtt_socket_client import mqtt_socket_client
import logging
import re
import json


class mqtt_server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_list = dict()
        self.client_id = 0
        self._log = logging.getLogger('my_perfect_project')
        self._log.setLevel(logging.DEBUG)
        fh = logging.FileHandler('my_perfect_project.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s :: mqtt_server :: %(levelname)s :: %(funcName)s(%(lineno)d) :: %(message)s')
        fh.setFormatter(formatter)
        self._log.addHandler(fh)
        self._log.info('Started')

        self.validate_size = re.compile("^[0-9]{3}$")

        self.override_dict = dict()

    def listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(None)
            self.client_id = self.client_id + 1
            self._log.info('Client with id {} started'.format(self.client_id))
            # client.clientId = self.client_id
            self.client_list[self.client_id] = mqtt_socket_client(
                client, self.client_id)
            threading.Thread(target=self.listenToClient,
                             args=(self.client_list[self.client_id], address)).start()

    def listenToClient(self, client, address):

        while True:
            try:
                # self._log.info('Client {} wait for data'.format(
                #     client.client_id))
                data = client.recv_msg(3).decode("utf-8")
                if self.validate_size.match(data):

                    msg_size = int(data)
                    #data = client.recv_msg(msg_size).decode("utf-8")
                    read_data = 0
                    data = ""
                    while read_data < msg_size:
                        data = data + \
                            client.recv_msg(msg_size-read_data).decode("utf-8")
                        read_data = len(data.encode())
                        if read_data < msg_size:
                            self._log.info('Client {} MOREEEEEE'.format(
                                client.client_id))

                    # self._log.info('Client {} new data'.format(data))
                    if data:
                        # Set the response to echo back the recieved data
                        # split to topic and message "topt:msg"
                        data_Str = data
                        result = re.search(r"(^[^:]{1,}):([^:]{0,}):(.{0,}$)", data_Str)
                        groups = result.groups()

                        topic = groups[0]
                        pyaload = groups[2]

                        if topic == "subscribe":
                            self._log.info(
                                'Client {} subscribe {}'.format(client.client_id, pyaload))
                            client.add_topic(pyaload)

                        elif topic == "override":
                            self.parse_override(pyaload)
                            pass

                        else:
                            if topic == "simulation/connected":
                                client.set_name(pyaload)
                            if topic in self.override_dict:
                                pyaload = self.override_dict[topic]
                            self.broadcastMsg(topic, pyaload)
                    else:
                        raise error('Client disconnected')
                else:
                    self.remove_client(client.client_id)
                    return False
            except:
                self.remove_client(client.client_id)
                return False

    def broadcastMsg(self, topic, msg):
        # self._log.info('Send topic {} message {}"'.format(topic, msg))
        for clientId in self.client_list.keys():
            try:
                self.client_list[clientId].send_msg(topic, msg)
            except:
                self.remove_client(clientId)

    def remove_client(self, clientId):
        client_name = self.client_list[clientId].client_name
        self._log.info(
            'Client {} disconnected with name {}'.format(clientId, client_name))
        self.client_list[clientId].close_client()
        del self.client_list[clientId]
        self.broadcastMsg("simulation/disconnected", client_name)

    def parse_override(self, message):
        data = json.loads(message)
        for signal in data:
            if signal['state'] == "normal":
                # remove if exist in list
                self.override_dict.pop(signal['name'], None)
            else:
                self.override_dict[signal['name']] = signal['value']


if __name__ == "__main__":
    mqtt_server('', 12345).listen()
