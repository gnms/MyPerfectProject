from mqtt_topic import mqtt_topic


def test_mqtt_topic():
    ifd = mqtt_topic()
    assert ifd.simulation.idle == "simulation/idle"

    assert ifd.environment.date_time == "environment/date_time"

    assert ifd.environment.date_time == ifd.environment.date_time
    assert ifd.environment.date_time != ifd.simulation.idle
