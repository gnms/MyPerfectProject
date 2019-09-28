from mqtt_client import mqtt_client
from panel_simulation_gui import panel_simulation_gui


class panel_simulation(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "PANEL_TIME")
        self.gui = panel_simulation_gui(self)
        self.gui.start()

    def setup(self):
        self.mqtt_topic.simulation.connected.subscribe()
        self.mqtt_topic.simulation.disconnected.subscribe()
        pass

    def handel_messages(self, topic):
        ''' All incomming message that the module have subscribe will
        come to this method.
        '''
        if self.mqtt_topic.environment.date_time == topic:
            self.mqtt_topic.environment.date_time.get_time()
            self.gui.date_time_is['text'] = str(
                self.mqtt_topic.environment.date_time.get_time())

        elif (self.mqtt_topic.simulation.connected == topic):
            new_client = self.mqtt_topic.simulation.connected.get_client_name()
            if not new_client in self.gui.client_list.get(0, "end"):
                self.gui.client_list.insert(
                    self.gui.client_list.size() + 1, new_client)
                self._log.info('Add client {}'.format(new_client))

        elif (self.mqtt_topic.simulation.disconnected == topic):
            remove_client = self.mqtt_topic.simulation.connected.get_client_name()
            if remove_client in self.gui.client_list.get(0, "end"):
                idx = self.gui.client_list.get(0, "end").index(remove_client)
                self.gui.client_list.delete(idx)
        #     self.delete_active_client(
        #         self.mqtt_topic.simulation.disconnected.get_client_name())
        #     self._log.info('Remove client {}'.format(
        #         self.mqtt_topic.simulation.disconnected.get_client_name()))

        # self._log.info('MATS = "{}"'.format(str(
        #     self.mqtt_topic.environment.date_time.payload)))


if __name__ == '__main__':
    panel_simulation = panel_simulation()

    panel_simulation.run()
