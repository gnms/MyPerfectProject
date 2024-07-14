from threading import Lock
from mqtt_base_topic import mqtt_base_topic, mqtt_bool_topic, mqtt_datetime_topic, mqtt_int_topic, mqtt_string_topic, mqtt_void_topic
class mqtt_topic_simulation (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.connected = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/connected')
        self.disconnected = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/disconnected')
        self.idle = mqtt_string_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/idle')
        self.verbose = mqtt_void_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/verbose')
        self.started = mqtt_bool_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/started')
        self.speed = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'simulation/speed')

class mqtt_topic_reset (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.value = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/reset/value')
        self.counter = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/reset/counter')

class mqtt_topic_message (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.time_start = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_start')
        self.time_ten_yard = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_ten_yard')
        self.time_twenty_yard = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_twenty_yard')
        self.time_thirty_yard = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_thirty_yard')
        self.time_fourty_yard = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'message/time_fourty_yard')
        self.reset = mqtt_topic_reset(self.message_to_send, self.message_dictonary, self.lock, 'message/reset')

class mqtt_topic_io (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.time_start = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_start')
        self.time_ten_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_ten_yard')
        self.time_twenty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_twenty_yard')
        self.time_thirty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_thirty_yard')
        self.time_fourty_yard = mqtt_int_topic(self.message_to_send, self.message_dictonary, self.lock, 'io/time_fourty_yard')

class mqtt_topic_environment (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.date_time = mqtt_datetime_topic(self.message_to_send, self.message_dictonary, self.lock, 'environment/date_time')

class mqtt_topic_ifd (mqtt_base_topic):
    def __init__(self):
        super().__init__([], dict(), Lock(), "")
        self.simulation = mqtt_topic_simulation(self.message_to_send, self.message_dictonary, self.lock, 'simulation')
        self.message = mqtt_topic_message(self.message_to_send, self.message_dictonary, self.lock, 'message')
        self.io = mqtt_topic_io(self.message_to_send, self.message_dictonary, self.lock, 'io')
        self.environment = mqtt_topic_environment(self.message_to_send, self.message_dictonary, self.lock, 'environment')
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
    def get_all_leafs(self):
        return [self.simulation.connected,
self.simulation.disconnected,
self.simulation.idle,
self.simulation.verbose,
self.simulation.started,
self.simulation.speed,
self.message.time_start,
self.message.time_ten_yard,
self.message.time_twenty_yard,
self.message.time_thirty_yard,
self.message.time_fourty_yard,
self.message.reset.value,
self.message.reset.counter,
self.io.time_start,
self.io.time_ten_yard,
self.io.time_twenty_yard,
self.io.time_thirty_yard,
self.io.time_fourty_yard,
self.environment.date_time]
