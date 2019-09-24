from mqtt_client import mqtt_client


class client_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "DAY_LIGHT")

    def setup(self):
        pass

    def handel_messages(self, topic):
        pass


if __name__ == '__main__':
    client_daylight = client_daylight()

    client_daylight.run()
