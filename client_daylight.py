from mqtt_client import mqtt_client


class client_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "DAY_LIGHT")

    def setup(self):
        self.subscribe("mats")
        self.subscribe("per")

    def handel_messages(self, topic, message):
        self._log.info('Client {} got topic = "{}" message = "{}"'.format(
            self.client_name, topic, message))


if __name__ == '__main__':
    client_daylight = client_daylight()

    client_daylight.run()
