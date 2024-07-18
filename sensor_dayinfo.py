from topics_types.mqtt_topic import time_to_string
from clients.mqtt_client import mqtt_client
import requests


class sensor_dayinfo(mqtt_client):
    def __init__(self):
        mqtt_client.__init__(self, "DAY_INFO")

    def environment_date_time(self, time):
        URL = time.strftime('https://api.dryg.net/dagar/v2.1/%Y/%m/%d')
        r = requests.get(url=URL)

        # extracting data in json format
        data = r.json()
        if 'arbetsfri dag' in data['dagar'][0]:
            working_day = data['dagar'][0]['arbetsfri dag'] == 'Nej'
            self.mqtt_topic.day_info.working_day.publish(working_day)

        if 'veckodag' in data['dagar'][0]:
            day_of_week_name = data['dagar'][0]['veckodag']
            self.mqtt_topic.day_info.name_of_day.publish(day_of_week_name)

        if 'namnsdag' in data['dagar'][0]:
            name_of_day = data['dagar'][0]['namnsdag']
            self.mqtt_topic.day_info.name_day.publish(name_of_day)
            
        if 'r\u00f6d dag' in data['dagar'][0]:
            red_day = data['dagar'][0]['r\u00f6d dag'] == 'Ja'
            self.mqtt_topic.day_info.red_day.publish(red_day)

        if 'helgdagsafton' in data['dagar'][0]:
            special_day = data['dagar'][0]['helgdagsafton']
            self.mqtt_topic.day_info.special_day.publish(special_day)

        if 'helgdag' in data['dagar'][0]:
            special_day = data['dagar'][0]['helgdag']
            self.mqtt_topic.day_info.special_day.publish(special_day)

    def setup(self):
        self.mqtt_topic.day_info.name_of_day.discovery("Name of day")


# "veckodag": "Torsdag", "arbetsfri dag": "Nej", "r\u00f6d dag": "Nej", "vecka": "18", "dag i vecka": "4", "helgdagsafton": "Valborgsm\u00e4ssoafton", "dag f\u00f6re arbetsfri helgdag": "Ja", "flaggdag": "Kung Carl XVI Gustafs f\u00f6delsedag"}]}

if __name__ == '__main__':
    sensor_dayinfo = sensor_dayinfo()
    
    sensor_dayinfo.run()
