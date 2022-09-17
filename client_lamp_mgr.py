
from mqtt_client import mqtt_client
import enum
import json


class lamp_controler():
    def __init__(self, lamp_data, logger):
        self.name = lamp_data["name"]
        self.code = lamp_data["code"]
        self.nigth_light = lamp_data["night"] == "yes"
        morgings = lamp_data["mornings"]
        self.work_morning = morgings["workday"] == "yes"
        self.other_morning = morgings["other"] == "yes"
        self.lamp_is_on = False
        self._log = logger

    def update(self, is_work_day, day_state):
        return_value = None
        old_state = self.lamp_is_on
        self.lamp_is_on = False

        if day_state == "NIGHT" and self.nigth_light:
            self.lamp_is_on = True

        if day_state == "MORNING":
            if is_work_day and self.work_morning:
                self.lamp_is_on = True

            if not is_work_day and self.other_morning:
                self.lamp_is_on = True
        if day_state == "DAY":
            pass
        if day_state == "EVENING":
            self.lamp_is_on = True

        if old_state != self.lamp_is_on:
            self._log.info("Change state on lamp ({}) from {} to {}".format(
                self.name, old_state, self.lamp_is_on))

            if self.lamp_is_on:
                return_value = "{{\"name\": \"{}\",\"state\": \"on\",\"code\": \"{}\"}}".format(
                    self.name, self.code)
            else:
                return_value = "{{\"name\": \"{}\",\"state\": \"off\",\"code\": \"{}\"}}".format(
                    self.name, self.code)

        return return_value


class client_lamp_mgr(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "LAMP_MGR")
        self.lamp_array = []
        self.is_work_day = None
        self.day_state = None

        # parse the confdiguration file
        with open('lamp_config.json', 'r') as myfile:
            data = myfile.read()

        lamp_data = json.loads(data)
        for lamp in lamp_data:
            self.lamp_array.append(lamp_controler(lamp, self._log))

    def environment_date_time(self, time):
        if (self.is_work_day != None and self.day_state != None):
            for lamp in self.lamp_array:
                lamp.update(self.is_work_day, self.day_state)

    def house_lamp_state(self, lamp_state):
        self.day_state = lamp_state

    def day_info_working_day(self, is_work_day):
        self.is_work_day = is_work_day


if __name__ == '__main__':
    client_lamp_mgr = client_lamp_mgr()

    client_lamp_mgr.run()
