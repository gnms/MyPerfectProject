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

    def get_payload(self):
        return (self.payload)

    def set_payload(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_disconnected:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/disconnected'] = self
        self.topic = 'simulation/disconnected'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/idle'] = self
        self.topic = 'simulation/idle'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self):
        self.lock.acquire()
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_started:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/started'] = self
        self.topic = 'simulation/started'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, status):
        self.payload = status

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, status):
        self.lock.acquire()
        message = (status)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation/speed'] = self
        self.topic = 'simulation/speed'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, scale):
        self.payload = scale

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, scale):
        self.lock.acquire()
        message = (scale)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['simulation'] = self
        self.topic = 'simulation'
        self.lock = lock
        self.connected = mqtt_topic_connected(
            self.message_to_send, message_dictonary, self.lock)
        self.disconnected = mqtt_topic_disconnected(
            self.message_to_send, message_dictonary, self.lock)
        self.idle = mqtt_topic_idle(
            self.message_to_send, message_dictonary, self.lock)
        self.verbose = mqtt_topic_verbose(
            self.message_to_send, message_dictonary, self.lock)
        self.started = mqtt_topic_started(
            self.message_to_send, message_dictonary, self.lock)
        self.speed = mqtt_topic_speed(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_date_time:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['environment/date_time'] = self
        self.topic = 'environment/date_time'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, time):
        self.payload = time

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, time):
        self.lock.acquire()
        message = time_to_string(time)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_is_dark_outside:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['environment/is_dark_outside'] = self
        self.topic = 'environment/is_dark_outside'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, state):
        self.payload = state

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, state):
        self.lock.acquire()
        message = (state)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['environment'] = self
        self.topic = 'environment'
        self.lock = lock
        self.date_time = mqtt_topic_date_time(
            self.message_to_send, message_dictonary, self.lock)
        self.is_dark_outside = mqtt_topic_is_dark_outside(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_outdoor_light:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/outdoor_light'] = self
        self.topic = 'sensors/outdoor_light'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return float(self.payload)

    def set_payload(self, light_value):
        self.payload = light_value

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, light_value):
        self.lock.acquire()
        message = (light_value)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sun_angle:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_angle'] = self
        self.topic = 'sensors/sun_angle'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return float(self.payload)

    def set_payload(self, sun_angle):
        self.payload = sun_angle

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_angle):
        self.lock.acquire()
        message = (sun_angle)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sun_noon:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_noon'] = self
        self.topic = 'sensors/sun_noon'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, sun_noon):
        self.payload = sun_noon

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_noon):
        self.lock.acquire()
        message = time_to_string(sun_noon)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sun_dawn:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_dawn'] = self
        self.topic = 'sensors/sun_dawn'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, sun_dawn):
        self.payload = sun_dawn

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_dawn):
        self.lock.acquire()
        message = time_to_string(sun_dawn)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sun_dusk:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_dusk'] = self
        self.topic = 'sensors/sun_dusk'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, sun_dusk):
        self.payload = sun_dusk

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_dusk):
        self.lock.acquire()
        message = time_to_string(sun_dusk)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sun_daylight:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/sun_daylight'] = self
        self.topic = 'sensors/sun_daylight'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return float(self.payload)

    def set_payload(self, sun_daylight):
        self.payload = sun_daylight

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, sun_daylight):
        self.lock.acquire()
        message = (sun_daylight)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_cloude:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors/cloude'] = self
        self.topic = 'sensors/cloude'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return float(self.payload)

    def set_payload(self, cloude):
        self.payload = cloude

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, cloude):
        self.lock.acquire()
        message = (cloude)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_sensors:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['sensors'] = self
        self.topic = 'sensors'
        self.lock = lock
        self.outdoor_light = mqtt_topic_outdoor_light(
            self.message_to_send, message_dictonary, self.lock)
        self.sun_angle = mqtt_topic_sun_angle(
            self.message_to_send, message_dictonary, self.lock)
        self.sun_noon = mqtt_topic_sun_noon(
            self.message_to_send, message_dictonary, self.lock)
        self.sun_dawn = mqtt_topic_sun_dawn(
            self.message_to_send, message_dictonary, self.lock)
        self.sun_dusk = mqtt_topic_sun_dusk(
            self.message_to_send, message_dictonary, self.lock)
        self.sun_daylight = mqtt_topic_sun_daylight(
            self.message_to_send, message_dictonary, self.lock)
        self.cloude = mqtt_topic_cloude(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_special_day:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info/special_day'] = self
        self.topic = 'day_info/special_day'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, name_on_day):
        self.payload = name_on_day

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, name_on_day):
        self.lock.acquire()
        message = (name_on_day)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_name_of_day:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info/name_of_day'] = self
        self.topic = 'day_info/name_of_day'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, name_of_day):
        self.payload = name_of_day

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, name_of_day):
        self.lock.acquire()
        message = (name_of_day)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_name_day:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info/name_day'] = self
        self.topic = 'day_info/name_day'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, name_day):
        self.payload = name_day

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, name_day):
        self.lock.acquire()
        message = (name_day)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_red_day:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info/red_day'] = self
        self.topic = 'day_info/red_day'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, red_day):
        self.payload = red_day

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, red_day):
        self.lock.acquire()
        message = (red_day)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_working_day:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info/working_day'] = self
        self.topic = 'day_info/working_day'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, working_day):
        self.payload = working_day

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, working_day):
        self.lock.acquire()
        message = (working_day)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_day_info:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['day_info'] = self
        self.topic = 'day_info'
        self.lock = lock
        self.special_day = mqtt_topic_special_day(
            self.message_to_send, message_dictonary, self.lock)
        self.name_of_day = mqtt_topic_name_of_day(
            self.message_to_send, message_dictonary, self.lock)
        self.name_day = mqtt_topic_name_day(
            self.message_to_send, message_dictonary, self.lock)
        self.red_day = mqtt_topic_red_day(
            self.message_to_send, message_dictonary, self.lock)
        self.working_day = mqtt_topic_working_day(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_is_awake:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['house/human/is_awake'] = self
        self.topic = 'house/human/is_awake'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, is_awake):
        self.payload = is_awake

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, is_awake):
        self.lock.acquire()
        message = (is_awake)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_human:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['house/human'] = self
        self.topic = 'house/human'
        self.lock = lock
        self.is_awake = mqtt_topic_is_awake(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_lamp_state:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['house/lamp_state'] = self
        self.topic = 'house/lamp_state'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return (self.payload)

    def set_payload(self, lamp_state):
        self.payload = lamp_state

    def create_message(self, topic, message):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}'.format(topic_str, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
                3, '0') + message_to_send
        return message_to_send

    def publish(self, lamp_state):
        self.lock.acquire()
        message = (lamp_state)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(
            self.create_message('subscribe', self.topic))
        self.lock.release()

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


class mqtt_topic_house:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['house'] = self
        self.topic = 'house'
        self.lock = lock
        self.human = mqtt_topic_human(
            self.message_to_send, message_dictonary, self.lock)
        self.lamp_state = mqtt_topic_lamp_state(
            self.message_to_send, message_dictonary, self.lock)


class mqtt_topic_ifd:
    def __init__(self):
        self.message_to_send = []
        message_dictonary = dict()
        lock = Lock()
        self.message_dictonary = message_dictonary
        self.lock = lock
        self.simulation = mqtt_topic_simulation(
            self.message_to_send, message_dictonary, self.lock)
        self.environment = mqtt_topic_environment(
            self.message_to_send, message_dictonary, self.lock)
        self.sensors = mqtt_topic_sensors(
            self.message_to_send, message_dictonary, self.lock)
        self.day_info = mqtt_topic_day_info(
            self.message_to_send, message_dictonary, self.lock)
        self.house = mqtt_topic_house(
            self.message_to_send, message_dictonary, self.lock)

    def subscribe_all(self):
        self.simulation.connected.subscribe()
        self.simulation.disconnected.subscribe()
        self.simulation.idle.subscribe()
        self.simulation.verbose.subscribe()
        self.simulation.started.subscribe()
        self.simulation.speed.subscribe()
        self.environment.date_time.subscribe()
        self.environment.is_dark_outside.subscribe()
        self.sensors.outdoor_light.subscribe()
        self.sensors.sun_angle.subscribe()
        self.sensors.sun_noon.subscribe()
        self.sensors.sun_dawn.subscribe()
        self.sensors.sun_dusk.subscribe()
        self.sensors.sun_daylight.subscribe()
        self.sensors.cloude.subscribe()
        self.day_info.special_day.subscribe()
        self.day_info.name_of_day.subscribe()
        self.day_info.name_day.subscribe()
        self.day_info.red_day.subscribe()
        self.day_info.working_day.subscribe()
        self.house.human.is_awake.subscribe()
        self.house.lamp_state.subscribe()

    def get_message_to_send(self):
        return self.message_to_send

    def clear_message_to_send(self):
        self.message_to_send.clear()

    def get_message(self, message_as_text):
        return self.message_dictonary[message_as_text]
