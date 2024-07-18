from topics_types.mqtt_topic import time_to_string
from clients.mqtt_client import mqtt_client
from pyowm import OWM
from astral.location import Location, LocationInfo
from astral.sun import sun
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo # Python 3.9


class sensor_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "SENSOR_LIGHT")
        #self.astral = Astral()
        #self.astral.solar_depression = 'civil'

        #self.city = self.astral["Stockholm"]
        self.city =  LocationInfo("Stockholm", "Sweden", "Europe/Stockholm", 59.3, 15.2)

        self.sun_angle_array = [-27, -7, -4, -3, 2, 5, 10, 70]
        self.daylight_sensor_value = [
            706429, 706429, 680000, 653996, 47542, 4707, 896, 56]

        owm = OWM('ad0fb07124008d74ebe6e3587b8cfbd1')
        mgr = owm.weather_manager()
        self.sf = mgr.weather_at_place('Garphyttan, SE')

    def environment_date_time(self, time):

        #sun = self.city.sun(date=time, local=True)
        s = sun(self.city.observer, date=time)
        solar_none = s['noon']
        solar_dawn = s['dawn']
        solar_dusk = s['dusk']
        solar_sunrise = s['sunrise']
        solar_sunset = s['sunset']
        #astral_day_light = self.city.daylight(time)
        #astral_day_light = (solar_sunset-solar_sunrise)
        solar_day_light = (solar_sunset-solar_sunrise).seconds/3600


        #sun_angle = Location(self.city).solar_azimuth(time)
        sun_angle = Location(self.city).solar_elevation(time)
        #weather = self.sf.get_weather()
        #sun_angle = self.city.solar_elevation(time)

        cloude = self.sf.weather.clouds
        outdoor_light = self.get_light_from_sun_angle(sun_angle)
        # self._log.info('Elevation = {}, daylight = {}, cloude = {}, solar_none = {}, solar_dawn = {}, solar_dusk = {}, solar_day_light = {}'.format(
        #     sun_angle, outdoor_light, cloude, solar_none, time_to_string(solar_dawn), time_to_string(solar_dusk), solar_day_light))

        self.mqtt_topic.sensors.cloude.publish(cloude)
        self.mqtt_topic.sensors.outdoor_light.publish(outdoor_light)
        self.mqtt_topic.sensors.sun_angle.publish(sun_angle)
        self.mqtt_topic.sensors.sun_noon.publish(solar_none)
        self.mqtt_topic.sensors.sun_dawn.publish(solar_dawn)
        self.mqtt_topic.sensors.sun_dusk.publish(solar_dusk)
        self.mqtt_topic.sensors.sun_daylight.publish(solar_day_light)

    def get_light_from_sun_angle(self, sun_angle):
        return np.interp(sun_angle, self.sun_angle_array, self.daylight_sensor_value)


if __name__ == '__main__':
    sensor_daylight = sensor_daylight()

    sensor_daylight.run()
