
from mqtt_client import mqtt_client
from panel_signal_mgr_gui import panel_signal_mgr_gui


class panel_signal_mgr(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "SIGNAL_MGR")
        self.gui = panel_signal_mgr_gui()

        self.gui.start()

    def setup(self):
        self.subscribe_with_method_name = False
        self.mqtt_topic.subscribe_all()

    def handel_messages(self, topic):
        self.gui.update_date(topic.topic, topic.get_payload())


if __name__ == '__main__':
    panel_signal_mgr = panel_signal_mgr()

    panel_signal_mgr.run()
