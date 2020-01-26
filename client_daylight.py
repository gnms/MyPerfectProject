from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
import math
from mqtt_client import mqtt_client
from astral import Astral
import numpy as np
from sklearn.externals import joblib


class client_daylight(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "DAY_LIGHT")
        self.astral = Astral()
        self.astral.solar_depression = 'civil'

        self.city = self.astral["Stockholm"]

        self.sun_angle_array = [-27, -7, -4, -3, 2, 5, 10, 70]
        self.daylight_sensor_value = [
            706429, 706429, 680000, 653996, 47542, 4707, 896, 56]

        self.joblib_model = joblib.load(
            "/home/dev/github/MyPerfectProject/log_reg_data")
        self.sun_angle = 0
        self.light_value = 0
        self.cloude_value = 0

    def setup(self):
        self.mqtt_topic.sensors.cloude.subscribe()
        self.mqtt_topic.sensors.sun_angle.subscribe()
        self.mqtt_topic.sensors.outdoor_light.subscribe()

    def handel_messages(self, topic):
        if self.mqtt_topic.environment.date_time == topic:
            Xnew = [[self.sun_angle, self.light_value, self.cloude_value]]
            value = self.joblib_model.predict(Xnew)
            self._log.info('day/night = {}'.format(
                value))

        if self.mqtt_topic.sensors.cloude == topic:
            self.cloude_value = self.mqtt_topic.sensors.cloude.get_cloude()
        if self.mqtt_topic.sensors.sun_angle == topic:
            self.sun_angle = self.mqtt_topic.sensors.sun_angle.get_sun_angle()
        if self.mqtt_topic.sensors.outdoor_light == topic:
            self.light_value = math.log(
                self.mqtt_topic.sensors.outdoor_light.get_light_value(), 1.3)


#   def setCurrentState(state, light, sun, cloud):
#         Xnew = [[sun, light, cloud]]
#         value = joblib_model.predict(Xnew)

#         if value == 0:
#             newState = 'dark'
#         else:
#             newState = 'light'

#         if newState != state:
#             logger.info(
#                 "Change light state from {} to {}".format(state, newState))
#         return newState
if __name__ == '__main__':
    client_daylight = client_daylight()

    client_daylight.run()
