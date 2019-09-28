from mqtt_client import mqtt_client
from astral import Astral


class client_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "DAY_LIGHT")
        self.astral = Astral()
        self.astral.solar_depression = 'civil'

        self.city = self.astral["Stockholm"]

    def setup(self):
        pass

    def handel_messages(self, topic):
        if self.mqtt_topic.environment.date_time == topic:
            sun_elev = self.city.solar_elevation(
                self.mqtt_topic.environment.date_time.get_time())
            self._log.info('Elevation = {}'.format(sun_elev))


if __name__ == '__main__':
    client_daylight = client_daylight()

    client_daylight.run()
