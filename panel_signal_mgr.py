
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

        if topic == self.mqtt_topic.io.time_start:
            pass
        self.gui.update_date(topic.topic, topic.get_payload())

        if topic == self.mqtt_topic.environment.date_time:
            # send all override to server
            meassage = self.gui.get_override()
            if meassage != None:
                message_to_send = '{}::{}'.format("override", meassage)
                message_to_send = str(len(message_to_send)).rjust(
                    3, '0') + message_to_send
                self.mqtt_topic.message_to_send.append(message_to_send)

            
            meassage = self.gui.get_send_message()
            if meassage != None:
                message_to_send = '{}::{}'.format("override", meassage)
                message_to_send = str(len(message_to_send)).rjust(
                    3, '0') + message_to_send
                self.mqtt_topic.message_to_send.append(message_to_send)


if __name__ == '__main__':
    panel_signal_mgr = panel_signal_mgr()

    panel_signal_mgr.run()
