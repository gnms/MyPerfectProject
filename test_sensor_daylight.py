from sensor_daylight import sensor_daylight
from topics_types.mqtt_topic import mqtt_topic_ifd
from topics_types.mqtt_topic import string_to_time


def test_daylight_model():
    client = sensor_daylight()
    mqtt_topic = mqtt_topic_ifd()

    mqtt_topic.environment.date_time.set_time(
        string_to_time("2020-03-07 08:00:00.000000"))

    # client.handel_messages(mqtt_topic.environment.date_time)


def test_light_from_sun_angle():
    client = sensor_daylight()
    assert 896 == client.get_light_from_sun_angle(10)
    assert 290123.6 == client.get_light_from_sun_angle(0)
    assert 532705.2 == client.get_light_from_sun_angle(-2)
    assert 706429 == client.get_light_from_sun_angle(-24)
