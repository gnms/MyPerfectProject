
import sys
import os

# Lägg till sökvägen till parent_module i sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
sys.path.insert(0, parent_dir)

from clients.mqtt_client import mqtt_client
from panels.panel_signal_mgr_gui import panel_signal_mgr_gui

## Class that inherit from mqtt_client and act as a client but also have a GUI where it is possibly
## to see and override each signals value.
class panel_signal_mgr(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "SIGNAL_MGR")

        ## Here the GUI is created and assigned to the gui parameter.
        ## GUI is also started here
        self.gui = panel_signal_mgr_gui(self.mqtt_topic)
        self.gui.start()

    def setup(self):
        ## we subscribe all signals
        self.subscribe_with_method_name = False
        self.mqtt_topic.subscribe_all()

    def handel_messages(self, topic):

        if topic == self.mqtt_topic.io.time_start:
            pass
        self.gui.update_date(topic.topic, topic.type_to_string())


if __name__ == '__main__':
    panel_signal_mgr = panel_signal_mgr()

    panel_signal_mgr.run()
