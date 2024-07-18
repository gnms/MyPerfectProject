import sys
import os

# Lägg till sökvägen till parent_module i sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
sys.path.insert(0, parent_dir)

from clients.mqtt_client import mqtt_client
from panel_simulation_gui import panel_simulation_gui


class panel_simulation(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "PANEL_TIME")
        self.gui = panel_simulation_gui(self)
        self.gui.start()
        self.online_client_list = []

    def environment_date_time(self, time):
        self.gui.date_time_is['text'] = str(time)

    def simulation_connected(self, client_name):
        try:
            if not client_name in self.gui.client_list.get(0, "end"):
                self.gui.client_list.insert(
                    self.gui.client_list.size() + 1, client_name)
                self._log.info('Add client {}'.format(client_name))
        except:
            self.online_client_list.append(client_name)

    def simulation_disconnected(self, client_name):
        self._log.info('trt to Delete client {}'.format(client_name))
        try:
            if client_name in self.gui.client_list.get(0, "end"):
                idx = self.gui.client_list.get(
                    0, "end").index(client_name)
                self.gui.client_list.delete(idx)
                self._log.info('Delete client {}'.format(client_name))
        except:
            pass

    def setup(self):
        self.mqtt_topic.simulation.verbose.publish()
        # def handel_messages(self, topic):
        #     ''' All incomming message that the module have subscribe will
        #     come to this method.
        #     '''

        #     elif (self.mqtt_topic.simulation.disconnected == topic):

        #             #     self.delete_active_client(
        #             #         self.mqtt_topic.simulation.disconnected.get_client_name())
        #             #     self._log.info('Remove client {}'.format(
        #             #         self.mqtt_topic.simulation.disconnected.get_client_name()))

        #             # self._log.info('MATS = "{}"'.format(str(
        #             #     self.mqtt_topic.environment.date_time.payload)))


if __name__ == '__main__':
    panel_simulation = panel_simulation()

    panel_simulation.run()
