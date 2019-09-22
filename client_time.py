from mqtt_client import mqtt_client
from enum import Enum
import threading


class CLIENT_STATES(Enum):
    IDLE = 1
    IN_PROGRESS = 2


class CLIENT_TIME_STATES(Enum):
    STOPED = 1
    RUNNING = 2


class client_time(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "TIME")
        self.active_clients = dict()
        self.state = CLIENT_TIME_STATES.STOPED
        self.scale = 1

    def setup(self):
        self.mqtt_topic.simulation.client.subscribe()
        self.mqtt_topic.simulation.idle.subscribe()
        self.mqtt_topic.simulation.start.subscribe()
        self.mqtt_topic.simulation.stop.subscribe()
        self.mqtt_topic.simulation.speed.subscribe()

        self.mqtt_topic.simulation.verbose.publish()

    def handel_messages(self, topic):
        ''' All incomming message that the module have subscribe will 
        come to this method.
        '''

        if (self.mqtt_topic.simulation.client == topic):
            self.add_active_client(
                self.mqtt_topic.simulation.client.get_client_name())
            self._log.info('CLIENT')

        elif (self.mqtt_topic.simulation.start == topic and self.state != CLIENT_TIME_STATES.RUNNING):
            self.state = CLIENT_TIME_STATES.RUNNING

            self.timer = threading.Timer(1/self.scale, self.update_time)
            self.timer.start()
            self._log.info('STARTED')
            pass
        elif (self.mqtt_topic.simulation.stop == topic and self.state != CLIENT_TIME_STATES.STOPED):
            self.state = CLIENT_TIME_STATES.STOPED
            self.timer.cancel()

            self._log.info('STOPED')
            pass
        elif (self.mqtt_topic.simulation.speed == topic):
            self.timer.cancel()
            self.scale = self.mqtt_topic.simulation.speed.get_scale() / 100
            self.timer = threading.Timer(1/self.scale, self.update_time)
            self.timer.start()
            self._log.info('SPEED')
            pass
        else:
            self._log.info('NONE')

        self._log.info('Client {} got topic = "{}"'.format(
            self.client_name, topic))

    def add_active_client(self, name_of_new_client):
        if name_of_new_client not in self.active_clients:
            self.active_clients[name_of_new_client] = CLIENT_STATES.IDLE

    def update_time(self):
        self.timer = threading.Timer(1/self.scale, self.update_time)
        self.timer.start()
        self._log.info('New Time')
        pass


if __name__ == '__main__':
    client_time = client_time()

    client_time.run()
