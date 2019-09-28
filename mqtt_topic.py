from datetime import datetime
from threading import Lock
def string_to_time(timeStr):
    return datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')
def time_to_string(_time):
    return _time.strftime('%Y-%m-%d %H:%M:%S.%f')




class mqtt_topic_connected:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/connected'] = self
        self.topic = 'simulation/connected'
        self.lock = lock
        self.payload = None

    def get_client_name(self):
        return (self.payload)

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
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_disconnected:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/disconnected'] = self
        self.topic = 'simulation/disconnected'
        self.lock = lock
        self.payload = None

    def get_client_name(self):
        return (self.payload)

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
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_idle:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/idle'] = self
        self.topic = 'simulation/idle'
        self.lock = lock
        self.payload = None

    def get_client_name(self):
        return (self.payload)

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
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_verbose:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/verbose'] = self
        self.topic = 'simulation/verbose'
        self.lock = lock

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
        self.lock.acquire()
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_started:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/started'] = self
        self.topic = 'simulation/started'
        self.lock = lock
        self.payload = None

    def get_status(self):
        return 'True' in(self.payload)

    def set_status(self, status):
        self.payload = status

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
           3, '0') + message_to_send
        return message_to_send

    def publish(self, status):
        self.lock.acquire()
        message = (status)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_speed:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/speed'] = self
        self.topic = 'simulation/speed'
        self.lock = lock
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
        self.lock.acquire()
        message = (scale)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_simulation:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation'] = self
        self.topic = 'simulation'
        self.lock = lock
        self.connected = mqtt_topic_connected(self.message_to_send, message_dictonary, self.lock)
        self.disconnected = mqtt_topic_disconnected(self.message_to_send, message_dictonary, self.lock)
        self.idle = mqtt_topic_idle(self.message_to_send, message_dictonary, self.lock)
        self.verbose = mqtt_topic_verbose(self.message_to_send, message_dictonary, self.lock)
        self.started = mqtt_topic_started(self.message_to_send, message_dictonary, self.lock)
        self.speed = mqtt_topic_speed(self.message_to_send, message_dictonary, self.lock)







class mqtt_topic_date_time:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['environment/date_time'] = self
        self.topic = 'environment/date_time'
        self.lock = lock
        self.payload = None

    def get_time(self):
        return string_to_time(self.payload)

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
        self.lock.acquire()
        message = time_to_string(time)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_environment:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['environment'] = self
        self.topic = 'environment'
        self.lock = lock
        self.date_time = mqtt_topic_date_time(self.message_to_send, message_dictonary, self.lock)







class mqtt_topic_outdoor_light:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/outdoor_light'] = self
        self.topic = 'sensors/outdoor_light'
        self.lock = lock
        self.payload = None

    def get_light_value(self):
        return (self.payload)

    def set_light_value(self, light_value):
        self.payload = light_value

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
           3, '0') + message_to_send
        return message_to_send

    def publish(self, light_value):
        self.lock.acquire()
        message = (light_value)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_sun_angle:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_angle'] = self
        self.topic = 'sensors/sun_angle'
        self.lock = lock
        self.payload = None

    def get_sun_angle(self):
        return (self.payload)

    def set_sun_angle(self, sun_angle):
        self.payload = sun_angle

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        message_to_send = str(len(message_to_send)).rjust(
           3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_angle):
        self.lock.acquire()
        message = (sun_angle)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False





class mqtt_topic_sensors:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors'] = self
        self.topic = 'sensors'
        self.lock = lock
        self.outdoor_light = mqtt_topic_outdoor_light(self.message_to_send, message_dictonary, self.lock)
        self.sun_angle = mqtt_topic_sun_angle(self.message_to_send, message_dictonary, self.lock)





class mqtt_topic_ifd:
    def __init__(self):
        self.message_to_send = []
        message_dictonary = dict()
        lock = Lock()
        self.message_dictonary = message_dictonary
        self.lock = lock
        self.simulation = mqtt_topic_simulation(self.message_to_send, message_dictonary, self.lock)
        self.environment = mqtt_topic_environment(self.message_to_send, message_dictonary, self.lock)
        self.sensors = mqtt_topic_sensors(self.message_to_send, message_dictonary, self.lock)

    def get_message_to_send(self):
        return self.message_to_send
    def clear_message_to_send(self):
        self.message_to_send.clear()
    def get_message(self, message_as_text):
        return self.message_dictonary[message_as_text]


