from mqtt_topic import mqtt_topic_ifd
from datetime import datetime
from dateutil import tz


class my_test_client():
    def __init__(self):
        self.send_msg = ""

    def create_message(self, topic, message):
        return "{}:{}".format(topic, message)

    def send_on_socket(self, message):
        self.send_msg = message


def test_mqtt_topic():
    ifd = mqtt_topic_ifd()
    assert ifd.simulation.idle == "simulation/idle"

    assert ifd.environment.date_time == "environment/date_time"

    assert ifd.environment.date_time == ifd.environment.date_time
    assert ifd.environment.date_time != ifd.simulation.idle


def test_mqtt_topic_subscribe():
    ifd = mqtt_topic_ifd()
    ifd.simulation.idle.subscribe()

    message_to_send = ifd.get_message_to_send()
    assert 1 == len(message_to_send)
    assert message_to_send[0] == "025subscribe:simulation/idle"

    ifd.simulation.started.subscribe()
    assert 2 == len(message_to_send)
    assert message_to_send[1] == "028subscribe:simulation/started"


def test_mqtt_topic_publish():
    ifd = mqtt_topic_ifd()
    ifd.simulation.idle.publish("Kalle")

    ifd.simulation.verbose.publish()

    message_to_send = ifd.get_message_to_send()
    assert 2 == len(message_to_send)
    assert message_to_send[0] == "021simulation/idle:Kalle"

    assert message_to_send[1] == "019simulation/verbose:"


def test_mqtt_topic_publish_bool():
    ifd = mqtt_topic_ifd()
    topic = ifd.get_message("simulation/started")

    topic.payload = "True"

    data = topic.get_status()
    assert data == True

    topic.payload = "False"

    data = topic.get_status()
    assert data == False


def test_mqtt_topic_publish_date_time():
    NYC = tz.gettz('Europe/Stockholm')
    ifd = mqtt_topic_ifd()
    t = datetime(2019, 9, 23, 18,
                 22, 23, 34, tzinfo=NYC)
    ifd.environment.date_time.publish(t)
    message_to_send = ifd.get_message_to_send()
    assert message_to_send[0] == "048environment/date_time:2019-09-23 18:22:23.000034"

    topic = ifd.get_message("environment/date_time")

    topic.payload = "2019-09-23 18:22:23.000034"

    #assert str(t) == str(topic.get_time())
