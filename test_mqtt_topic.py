from mqtt_topic import mqtt_topic_ifd


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

    ifd.simulation.start.subscribe()
    assert 2 == len(message_to_send)
    assert message_to_send[1] == "026subscribe:simulation/start"


def test_mqtt_topic_publish():
    ifd = mqtt_topic_ifd()
    ifd.simulation.idle.publish("Kalle")

    ifd.simulation.verbose.publish()

    message_to_send = ifd.get_message_to_send()
    assert 2 == len(message_to_send)
    assert message_to_send[0] == "021simulation/idle:Kalle"

    assert message_to_send[1] == "019simulation/verbose:"
