from mqtt_client import mqtt_client
from astral import Astral
import numpy as np
import pyowm


class sensor_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "SENSOR_LIGHT")
        self.astral = Astral()
        self.astral.solar_depression = 'civil'

        self.city = self.astral["Stockholm"]

        self.sun_angle_array = [-27, -7, -4, -3, 2, 5, 10, 70]
        self.daylight_sensor_value = [
            706429, 706429, 680000, 653996, 47542, 4707, 896, 56]

        owm = pyowm.OWM('ad0fb07124008d74ebe6e3587b8cfbd1')
        self.sf = owm.weather_at_place('Garphyttan, SE')

    def setup(self):
        pass

    def handel_messages(self, topic):
        if self.mqtt_topic.environment.date_time == topic:
            weather = self.sf.get_weather()
            sun_angle = self.city.solar_elevation(
                self.mqtt_topic.environment.date_time.get_time())
            cloude = weather.get_clouds()
            outdoor_light = self.get_light_from_sun_angle(sun_angle)
            self._log.info('Elevation = {}, daylight = {}, cloude = {}'.format(
                sun_angle, outdoor_light, cloude))

            self.mqtt_topic.sensors.cloude.publish(cloude)
            self.mqtt_topic.sensors.outdoor_light.publish(outdoor_light)
            self.mqtt_topic.sensors.sun_angle.publish(sun_angle)

    def get_light_from_sun_angle(self, sun_angle):
        return np.interp(sun_angle, self.sun_angle_array, self.daylight_sensor_value)


if __name__ == '__main__':
    sensor_daylight = sensor_daylight()

    sensor_daylight.run()
