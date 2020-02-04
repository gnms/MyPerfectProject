
from mqtt_client import mqtt_client
import enum

# Using enum class create enumerations


class LightMgrStates(enum.Enum):
    NIGHT_LIGHT = 1
    DAY_LIGHT = 2
    MORNING_LIGHT = 3
    EVENING_LIGHT = 4


class client_light_mgr(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "LIGHT_MGR")
        self.state = LightMgrStates.NIGHT_LIGHT
        self.is_dark = False
        self.is_awake = False
        self.time_at_none = None
        self.time_at_down = None

    def environment_date_time(self, time):
        if self.state == LightMgrStates.NIGHT_LIGHT:
            if self.is_dark:
                if self.is_awake:
                    if self.time_at_none > time:
                        self.state = LightMgrStates.MORNING_LIGHT
                        self._log.info('Chnage state to = MORNING_LIGHT')
                    else:
                        self.state = LightMgrStates.EVENING_LIGHT
                        self._log.info('Chnage state to EVENING_LIGHT')
            else:
                self.state = LightMgrStates.DAY_LIGHT
                self._log.info('Chnage state to DAY_LIGHT')

        elif self.state == LightMgrStates.MORNING_LIGHT:
            if self.is_dark:
                if self.time_at_none < time:
                    self.state = LightMgrStates.EVENING_LIGHT
                    self._log.info('Chnage state to EVENING_LIGHT')
            else:
                self.state = LightMgrStates.DAY_LIGHT
                self._log.info('Chnage state to DAY_LIGHT')

        elif self.state == LightMgrStates.DAY_LIGHT:
            if self.is_dark:
                self.state = LightMgrStates.EVENING_LIGHT
                self._log.info('Chnage state to EVENING_LIGHT')

        elif self.state == LightMgrStates.EVENING_LIGHT:
            if self.is_awake:
                if self.time_at_down < time and time < self.time_at_none:
                    self.state = LightMgrStates.MORNING_LIGHT
                    self._log.info('Chnage state to = MORNING_LIGHT')
            else:
                self.state = LightMgrStates.NIGHT_LIGHT
                self._log.info('Chnage state to NIGHT_LIGHT')

        self.send_lamp_state()

    def send_lamp_state(self):
        if self.state == LightMgrStates.NIGHT_LIGHT:
            self.mqtt_topic.house.lamp_state.publish("NIGHT")

        elif self.state == LightMgrStates.MORNING_LIGHT:
            self.mqtt_topic.house.lamp_state.publish("MORNING")

        elif self.state == LightMgrStates.DAY_LIGHT:
            self.mqtt_topic.house.lamp_state.publish("DAY")

        elif self.state == LightMgrStates.EVENING_LIGHT:
            self.mqtt_topic.house.lamp_state.publish("EVENING")

    def environment_is_dark_outside(self, is_dark_outside):
        self.is_dark = is_dark_outside

    def house_human_is_awake(self, is_awake):
        self.is_awake = is_awake

    def sensors_sun_noon(self, time_at_none):
        self.time_at_none = time_at_none

    def sensors_sun_dusk(self, time_at_dusk):
        self.time_at_dusk = time_at_dusk


if __name__ == '__main__':
    client_light_mgr = client_light_mgr()

    client_light_mgr.run()
