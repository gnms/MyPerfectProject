

class mqtt_topic_client:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/client'] = self
        self.topic = 'simulation/client'
        self.payload = None

    def get_client_name(self):
        return str(self.payload)

    def set_client_name(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        message = client_name
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_idle:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/idle'] = self
        self.topic = 'simulation/idle'
        self.payload = None

    def get_client_name(self):
        return str(self.payload)

    def set_client_name(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        message = client_name
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_verbose:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/verbose'] = self
        self.topic = 'simulation/verbose'

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self):
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_start:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/start'] = self
        self.topic = 'simulation/start'

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self):
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_stop:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/stop'] = self
        self.topic = 'simulation/stop'

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self):
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_speed:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation/speed'] = self
        self.topic = 'simulation/speed'
        self.payload = None

    def get_scale(self):
        return int(self.payload)

    def set_scale(self, scale):
        self.payload = scale

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self, scale):
        message = scale
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_simulation:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['simulation'] = self
        self.topic = 'simulation'
        self.client = mqtt_topic_client(
            self.message_to_send, message_dictonary)
        self.idle = mqtt_topic_idle(self.message_to_send, message_dictonary)
        self.verbose = mqtt_topic_verbose(
            self.message_to_send, message_dictonary)
        self.start = mqtt_topic_start(self.message_to_send, message_dictonary)
        self.stop = mqtt_topic_stop(self.message_to_send, message_dictonary)
        self.speed = mqtt_topic_speed(self.message_to_send, message_dictonary)


class mqtt_topic_date_time:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['environment/date_time'] = self
        self.topic = 'environment/date_time'
        self.payload = None

    def get_time(self):
        return str(self.payload)

    def set_time(self, time):
        self.payload = time

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
            3, '0') + message_to_send
        return message_to_send

    def publish(self, time):
        message = time
        self.message_to_send.append(self.create_message(self.topic, message))

    def subscribe(self):
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False


class mqtt_topic_environment:
    def __init__(self, message_to_send, message_dictonary):
        self.message_to_send = message_to_send
        message_dictonary['environment'] = self
        self.topic = 'environment'
        self.date_time = mqtt_topic_date_time(
            self.message_to_send, message_dictonary)


class mqtt_topic_ifd:
    def __init__(self):
        self.message_to_send = []
        message_dictonary = dict()
        self.message_dictonary = message_dictonary
        self.simulation = mqtt_topic_simulation(
            self.message_to_send, message_dictonary)
        self.environment = mqtt_topic_environment(
            self.message_to_send, message_dictonary)

    def get_message_to_send(self):
        return self.message_to_send

    def clear_message_to_send(self):
        self.message_to_send = []

    def get_message(self, message_as_text):
        return self.message_dictonary[message_as_text]
