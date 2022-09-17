from mqtt_client import mqtt_client
from enum import Enum
import threading
from datetime import datetime, timedelta
from dateutil import tz
import time
NYC = tz.gettz('Europe/Stockholm')


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
        self.getTime()
        self.timer = None

        if __debug__ != False:
            self.timer = threading.Timer(1, self.update_time)
            self.timer.start()

    # def setup(self):
    #     self.mqtt_topic.simulation.connected.subscribe()
    #     self.mqtt_topic.simulation.disconnected.subscribe()
    #     self.mqtt_topic.simulation.idle.subscribe()
    #     self.mqtt_topic.simulation.started.subscribe()
    #     self.mqtt_topic.simulation.speed.subscribe()

    #     self.mqtt_topic.simulation.verbose.publish()

    def simulation_connected(self, client_name):
        self.add_active_client(client_name)
        self._log.info('Add client {}'.format(client_name))

    def simulation_disconnected(self, client_name):
        self.delete_active_client(client_name)
        self._log.info('Remove client {}'.format(client_name))

        # Check if times in not running
        if self.timer == None and self.is_all_clients_idle():
            if self.state == CLIENT_TIME_STATES.RUNNING:
                self.update_time_sim()

    def simulation_idle(self, client_name):
        self.active_clients[client_name] = CLIENT_STATES.IDLE

        # Check if times in not running
        if self.timer == None and self.is_all_clients_idle():
            if self.state == CLIENT_TIME_STATES.RUNNING:
                self.update_time_sim()

    def environment_date_time(self, time):
        if self.state == CLIENT_TIME_STATES.STOPED:
            self.simulation_time = time

    def simulation_started(self, started):
        if self.state == CLIENT_TIME_STATES.STOPED and started:
            self.state = CLIENT_TIME_STATES.RUNNING
            self.timer = threading.Timer(1/self.scale, self.update_time_sim)
            self.timer.start()
            self._log.info('STARTED')

        elif (self.state == CLIENT_TIME_STATES.RUNNING and not started):
            self.state = CLIENT_TIME_STATES.STOPED
            if self.timer != None:
                self.timer.cancel()
                self.timer = None
            self._log.info('STOPED')

    def simulation_speed(self, speed):
        self.scale = speed / 100
        if self.state == CLIENT_TIME_STATES.RUNNING:
            if self.timer != None:
                self.timer.cancel()
                self.timer = None
            self.timer = threading.Timer(1/self.scale, self.update_time_sim)
            self.timer.start()
        self._log.info('SPEED')

    # def simulation_verbose(self):
    #     pass

    def getTime(self):
        currentTime = datetime.now()
        self.simulation_time = datetime(currentTime.year, currentTime.month, currentTime.day, currentTime.hour,
                                        currentTime.minute, currentTime.second, currentTime.microsecond, tzinfo=NYC)

    def step_milliseconds(self, mSec):
        self.simulation_time = self.simulation_time + \
            timedelta(microseconds=mSec*1000)

    def add_active_client(self, name_of_new_client):
        if name_of_new_client not in self.active_clients:
            self.active_clients[name_of_new_client] = CLIENT_STATES.IDLE

    def delete_active_client(self, name_of_client):
        if name_of_client in self.active_clients:
            del self.active_clients[name_of_client]

    def update_time_sim(self):
        if self.is_all_clients_idle():
            # set all to in progress
            for client_name in self.active_clients:
                self.active_clients[client_name] = CLIENT_STATES.IN_PROGRESS

            self.timer = threading.Timer(1/self.scale, self.update_time_sim)
            self.timer.start()
            #self._log.info('New Time = {}'.format(self.simulation_time))
            self.step_milliseconds(60000)
            self.mqtt_topic.environment.date_time.publish(self.simulation_time)
            self.send_message_to_server()
        else:
            self.timer = None

    def update_time(self):
        while True:
            self.getTime()
            self.mqtt_topic.environment.date_time.publish(self.simulation_time)
            self.send_message_to_server()
            time.sleep(1)

    def is_all_clients_idle(self):
        for client_name in self.active_clients:
            if self.active_clients[client_name] == CLIENT_STATES.IN_PROGRESS:
                return False

        return True


if __name__ == '__main__':
    client_time = client_time()

    client_time.run()
