from mqtt_client import mqtt_client
from panel_time_gui import panel_time_gui


class panel_time(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "PANEL_TIME")
        self.gui = panel_time_gui(self)
        self.gui.start()

    def setup(self):
        pass

    def handel_messages(self, topic):
        ''' All incomming message that the module have subscribe will
        come to this method.
        '''
        if self.mqtt_topic.environment.date_time == topic:
            self.mqtt_topic.environment.date_time.get_time()
            self.gui.date_time_is['text'] = str(
                self.mqtt_topic.environment.date_time.get_time())

        # self._log.info('MATS = "{}"'.format(str(
        #     self.mqtt_topic.environment.date_time.payload)))


if __name__ == '__main__':
    panel_time = panel_time()

    panel_time.run()
