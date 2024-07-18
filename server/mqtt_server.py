import threading
import socket
from mqtt_socket_client import mqtt_socket_client
import logging
import re
import json

## This is a class that act as a mqtt server instead of a real mqtt server.
## With this mqtt server is it possibly to override signals with other values
class mqtt_server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        ## list with all client that is connected to the server, all clients will be stored in teh list with 
        ## there id as a key in the dictonary.
        ## all clients will be stored in class mqtt_socket_client
        self.client_list = dict()

        ## A internal counter that incresae each time a new client is connected to the server
        ## the counter will never decresae eaven if teh client will be diconnected
        self.client_id = 0

        ## Start a logger fo debug
        self._log = logging.getLogger('my_perfect_project')
        self._log.setLevel(logging.DEBUG)
        fh = logging.FileHandler('my_perfect_project.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s :: mqtt_server :: %(levelname)s :: %(funcName)s(%(lineno)d) :: %(message)s')
        fh.setFormatter(formatter)
        self._log.addHandler(fh)
        self._log.info('Started')

        ## Regex to validate the incoming data, teh data shall always start with 3 digits that is the size of the message
        self.validate_size = re.compile("^[0-9]{3}$")

        ## A dictonary with all signals that are overidden. the keuy in teh dictonary is the name of the signal
        ## the value is eth ovrridden value.
        self.override_dict = dict()


    ## function that listen to new cennected clients, when a client is connected to the server this function is called
    ## The client will be stored in the client dictonary
    def listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        while True:
            ## wait for a client to connect to the server
            client, address = self.sock.accept()
            client.settimeout(None)

            ## increase the client id for the dictonary
            self.client_id = self.client_id + 1
            self._log.info('Client with id {} started'.format(self.client_id))
            # client.clientId = self.client_id

            ## Create the class mqtt_socket_client and set id and the socket for the cilent
            ## then start a thread that will listen to the client for data incomming fro teh client.
            ## when client send data to the server function listenToClient will be called and in that function the data will be parsed
            self.client_list[self.client_id] = mqtt_socket_client(
                client, self.client_id)
            threading.Thread(target=self.listenToClient,
                             args=(self.client_list[self.client_id], address)).start()

    ## Functioon that is a callback when data is recived from a client.
    def listenToClient(self, client, address):

        while True:
            try:
                # self._log.info('Client {} wait for data'.format(
                #     client.client_id))
                ## first read 3 byte that is the message size, that is how many byte the 
                ## actual data contains, the size shall be three digits 001 - 999
                ## the data is validated against a regex pattern.
                ## if the data is not a valid numder between 001 - 999
                ## we disconnec the client and end the thread
                data = client.recv_msg(3).decode("utf-8")
                if self.validate_size.match(data):
                    ## convert the text string as is a number to an integer
                    msg_size = int(data)
                    #data = client.recv_msg(msg_size).decode("utf-8")

                    ## now it is time to read the actual data that are sent in the message
                    ## we read to we got all bytes
                    read_data = 0
                    data = ""
                    while read_data < msg_size:
                        data = data + client.recv_msg(msg_size-read_data).decode("utf-8")
                        read_data = len(data.encode())
                        if read_data < msg_size:
                            self._log.info('Client {} MOREEEEEE'.format(client.client_id))

                    self._log.info('Client {} new data'.format(data))
                    if data:
                        # Set the response to echo back the recieved data
                        # split to topic and message "topt:msg"
                        ## the data have the following format topic:???:payload
                        ## we pase the message aand then we deside what to do
                        ## subscribe -> subscribe to a topic, we add the topic to the client insance subscribe::environment/date_time
                        ## overide -> if we shall overide a topic/signals value
                        ## simulation/connected -> the new connected client send its name on this topic.
                        data_Str = data
                        #self._log.info('regexdata {}'.format(data))
                        result = re.search(r"(^[^:]{1,}):([^:]{0,}):(.{0,}$)", data_Str)
                        groups = result.groups()

                        topic = groups[0]
                        pyaload = groups[2]

                        if topic == "subscribe":
                            self._log.info('Client {} subscribe {}'.format(client.client_id, pyaload))
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
                    self._log.info('Client {} disconnected, no valid data'.format(client.client_id))
                    self.remove_client(client.client_id)
                    return False
            except Exception as e:
                self._log.error(f"Client {client.client_id} disconnected exception", exc_info=True)               
                self.remove_client(client.client_id)
                return False

    def broadcastMsg(self, topic, msg):
        self._log.info('Send topic {} message {}"'.format(topic, msg))
        for clientId in self.client_list.keys():
            try:
                self.client_list[clientId].send_msg(topic, msg)
            except:
                self.remove_client(clientId)

    def remove_client(self, clientId):
        client_name = self.client_list[clientId].client_name
        self._log.info('Client {} disconnected with name {}'.format(clientId, client_name))
        self.client_list[clientId].close_client()
        del self.client_list[clientId]
        self.broadcastMsg("simulation/disconnected", client_name)

    def parse_override(self, message):
        try:
            data = json.loads(message)
        except ValueError as e:
            self._log.info('invalid json: %s' % e)
            return None # or: raise
        if data['state'] == "normal":
            # remove if exist in list
            self.override_dict.pop(data['name'], None)
        else:
            self.override_dict[data['name']] = data['value']


if __name__ == "__main__":
    mqtt_server('', 12345).listen()
