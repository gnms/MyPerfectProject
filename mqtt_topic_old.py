from datetime import datetime
from threading import Lock
import re
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

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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

    def get_payload(self):
        return (self.payload)

    def set_payload(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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

    def get_payload(self):
        return (self.payload)

    def set_payload(self, client_name):
        self.payload = client_name

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, client_name):
        self.lock.acquire()
        message = (client_name)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self):
        self.lock.acquire()
        message = ''
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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

    def get_payload(self):
        return 'True' in(self.payload)

    def set_payload(self, status):
        self.payload = status

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, status):
        self.lock.acquire()
        message = (status)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, scale):
        self.payload = scale

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, scale):
        self.lock.acquire()
        message = (scale)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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







class mqtt_topic_time_start:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/time_start'] = self
        self.topic = 'message/time_start'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, start):
        self.payload = start

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, start):
        self.lock.acquire()
        message = time_to_string(start)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_ten_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/time_ten_yard'] = self
        self.topic = 'message/time_ten_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, ten_yard):
        self.payload = ten_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, ten_yard):
        self.lock.acquire()
        message = time_to_string(ten_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_twenty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/time_twenty_yard'] = self
        self.topic = 'message/time_twenty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, twenty_yard):
        self.payload = twenty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, twenty_yard):
        self.lock.acquire()
        message = time_to_string(twenty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_thirty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/time_thirty_yard'] = self
        self.topic = 'message/time_thirty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, thirty_yard):
        self.payload = thirty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, thirty_yard):
        self.lock.acquire()
        message = time_to_string(thirty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_fourty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/time_fourty_yard'] = self
        self.topic = 'message/time_fourty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return string_to_time(self.payload)

    def set_payload(self, fourty_yard):
        self.payload = fourty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, fourty_yard):
        self.lock.acquire()
        message = time_to_string(fourty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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







class mqtt_topic_value:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/reset/value'] = self
        self.topic = 'message/reset/value'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, value):
        self.payload = value

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, value):
        self.lock.acquire()
        message = (value)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_counter:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/reset/counter'] = self
        self.topic = 'message/reset/counter'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, counter):
        self.payload = counter

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, counter):
        self.lock.acquire()
        message = (counter)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_reset:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message/reset'] = self
        self.topic = 'message/reset'
        self.lock = lock
        self.value = mqtt_topic_value(self.message_to_send, message_dictonary, self.lock)
        self.counter = mqtt_topic_counter(self.message_to_send, message_dictonary, self.lock)





class mqtt_topic_message:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['message'] = self
        self.topic = 'message'
        self.lock = lock
        self.time_start = mqtt_topic_time_start(self.message_to_send, message_dictonary, self.lock)
        self.time_ten_yard = mqtt_topic_time_ten_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_twenty_yard = mqtt_topic_time_twenty_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_thirty_yard = mqtt_topic_time_thirty_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_fourty_yard = mqtt_topic_time_fourty_yard(self.message_to_send, message_dictonary, self.lock)
        self.reset = mqtt_topic_reset(self.message_to_send, message_dictonary, self.lock)







class mqtt_topic_time_start:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io/time_start'] = self
        self.topic = 'io/time_start'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, start):
        self.payload = start

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, start):
        self.lock.acquire()
        message = (start)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_ten_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io/time_ten_yard'] = self
        self.topic = 'io/time_ten_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, ten_yard):
        self.payload = ten_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, ten_yard):
        self.lock.acquire()
        message = (ten_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_twenty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io/time_twenty_yard'] = self
        self.topic = 'io/time_twenty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, twenty_yard):
        self.payload = twenty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, twenty_yard):
        self.lock.acquire()
        message = (twenty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_thirty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io/time_thirty_yard'] = self
        self.topic = 'io/time_thirty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, thirty_yard):
        self.payload = thirty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, thirty_yard):
        self.lock.acquire()
        message = (thirty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_time_fourty_yard:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io/time_fourty_yard'] = self
        self.topic = 'io/time_fourty_yard'
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return int(self.payload)

    def set_payload(self, fourty_yard):
        self.payload = fourty_yard

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, fourty_yard):
        self.lock.acquire()
        message = (fourty_yard)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
        self.lock.release()

    def override(self, override, value):
        if override == True:
            override_str = "override"
        else:
            override_str = "normal"

        payload = "{{\"name\": \"{}\",\"state\": \"{}\",\"value\": \"{}\" }}".format(
                self.topic, override_str, value)
        
        self.lock.acquire()
        self.message_to_send.append(self.create_message('override', payload))
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





class mqtt_topic_io:
    def __init__(self, message_to_send, message_dictonary, lock):
        self.message_to_send = message_to_send
        message_dictonary['io'] = self
        self.topic = 'io'
        self.lock = lock
        self.time_start = mqtt_topic_time_start(self.message_to_send, message_dictonary, self.lock)
        self.time_ten_yard = mqtt_topic_time_ten_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_twenty_yard = mqtt_topic_time_twenty_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_thirty_yard = mqtt_topic_time_thirty_yard(self.message_to_send, message_dictonary, self.lock)
        self.time_fourty_yard = mqtt_topic_time_fourty_yard(self.message_to_send, message_dictonary, self.lock)







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

    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, time):
        self.lock.acquire()
        message = time_to_string(time)
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()

    def discovery(self, name):
        self.lock.acquire()
        string = re.sub(r"\/.{1,}\/", "/", self.topic)
        config = "{\"name\":\""+name+"\", \"state_topic\":\""+self.topic+"\", \"frc_upd\":\"true\"}"
        self.message_to_send.append(self.create_message("homeassistant/"+string+ "/config", config, "Retain"))
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





class mqtt_topic_ifd:
    def __init__(self):
        self.message_to_send = []
        message_dictonary = dict()
        lock = Lock()
        self.message_dictonary = message_dictonary
        self.lock = lock
        self.simulation = mqtt_topic_simulation(self.message_to_send, message_dictonary, self.lock)
        self.message = mqtt_topic_message(self.message_to_send, message_dictonary, self.lock)
        self.io = mqtt_topic_io(self.message_to_send, message_dictonary, self.lock)
        self.environment = mqtt_topic_environment(self.message_to_send, message_dictonary, self.lock)

    def subscribe_all(self):
        self.simulation.connected.subscribe()
        self.simulation.disconnected.subscribe()
        self.simulation.idle.subscribe()
        self.simulation.verbose.subscribe()
        self.simulation.started.subscribe()
        self.simulation.speed.subscribe()
        self.message.time_start.subscribe()
        self.message.time_ten_yard.subscribe()
        self.message.time_twenty_yard.subscribe()
        self.message.time_thirty_yard.subscribe()
        self.message.time_fourty_yard.subscribe()
        self.message.reset.value.subscribe()
        self.message.reset.counter.subscribe()
        self.io.time_start.subscribe()
        self.io.time_ten_yard.subscribe()
        self.io.time_twenty_yard.subscribe()
        self.io.time_thirty_yard.subscribe()
        self.io.time_fourty_yard.subscribe()
        self.environment.date_time.subscribe()

    def get_message_to_send(self):
        return self.message_to_send
    def clear_message_to_send(self):
        self.message_to_send.clear()
    def get_message(self, message_as_text):
        return self.message_dictonary[message_as_text]


