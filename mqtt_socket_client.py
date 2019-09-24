

class mqtt_socket_client:
    def __init__(self, socket_client, client_id):
        self.socket = socket_client
        self.topic_list = list()
        self.client_id = client_id
        self.client_name = ""

    def set_name(self, name):
        self.client_name = name

    def add_topic(self, topic):
        # Check if we have topic in list, if we do not have it we add it to topic list
        # Then we add subscriber to list
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.get_topic()
        if not topic_str in self.topic_list:
            self.topic_list.append(topic_str)

    def send_msg(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.get_topic()

        message_to_send = '{}:{}'.format(topic_str, message)

        if topic_str in self.topic_list:

            msg_to_send = str(len(message_to_send)).rjust(
                3, '0') + message_to_send
            self.socket.send(msg_to_send.encode())

    def close_client(self):
        self.socket.close()

    def recv_msg(self, size):
        return self.socket.recv(size)
