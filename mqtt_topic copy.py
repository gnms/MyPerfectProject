from datetime import datetime
from threading import Lock
from topics_types.mqtt_base_topic import mqtt_base_topic, mqtt_string_topic, mqtt_int_topic, mqtt_time_topic, mqtt_bool_topic


import re
def string_to_time(timeStr):
    return datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')
def time_to_string(_time):
    return _time.strftime('%Y-%m-%d %H:%M:%S.%f')




class mqtt_topic_simulation (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock):
        super().__init__(message_to_send, message_dictonary, lock, 'simulation')
        self.connected = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/disconnected')
        self.disconnected = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/disconnected')
        self.idle = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/idle')
        self.verbose = mqtt_base_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/verbose')
        self.started = mqtt_bool_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/started')
        self.speed = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/speed')


class mqtt_topic_reset (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock):
        super().__init__(message_to_send, message_dictonary, lock, 'message/reset')
        self.value = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/reset/value')
        self.counter = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/reset/counter')

class mqtt_topic_message (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock):
        super().__init__(message_to_send, message_dictonary, lock, 'message')
        self.time_start = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_start')
        self.time_ten_yard = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_ten_yard')
        self.time_twenty_yard = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_twenty_yard')
        self.time_thirty_yard = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_thirty_yard')
        self.time_fourty_yard = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_fourty_yard')
        self.reset = mqtt_topic_reset(self.message_to_send, self.message_dictonary, self.lock)



class mqtt_topic_io (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock):
        super().__init__(message_to_send, message_dictonary, lock, 'io')
        self.time_start = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_start')
        self.time_ten_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_ten_yard')
        self.time_twenty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_twenty_yard')
        self.time_thirty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_thirty_yard')
        self.time_fourty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_fourty_yard')


class mqtt_topic_environment (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock):
        super().__init__(message_to_send, message_dictonary, lock, 'environment')
        self.date_time = mqtt_time_topic(self.message_to_send, self.message_dictonary, self.lock, 'environment/date_time')

class mqtt_topic_ifd (mqtt_base_topic):
    def __init__(self):
        super().__init__([], dict(), Lock(), "")
        self.simulation = mqtt_topic_simulation(self.message_to_send, self.message_dictonary, self.lock)
        self.message = mqtt_topic_message(self.message_to_send, self.message_dictonary, self.lock)
        self.io = mqtt_topic_io(self.message_to_send, self.message_dictonary, self.lock)
        self.environment = mqtt_topic_environment(self.message_to_send, self.message_dictonary, self.lock)
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
