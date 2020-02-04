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

    def sensors_cloude(self, cloude_value):
        self.cloude_value = cloude_value

    def sensors_sun_angle(self, sun_angle):
        self.sun_angle = sun_angle

    def sensors_outdoor_light(self, light_value):
        self.light_value = math.log(light_value, 1.3)

    def environment_date_time(self, time):
        Xnew = [[self.sun_angle, self.light_value, self.cloude_value]]
        value = self.joblib_model.predict(Xnew)
        # self._log.info('day/night = {}'.format(
        #     value))

        if value == 1:
            self.mqtt_topic.environment.is_dark_outside.publish(False)
        else:
            self.mqtt_topic.environment.is_dark_outside.publish(True)


if __name__ == '__main__':
    client_daylight = client_daylight()

    client_daylight.run()
