#import mqtt_base_topic
#from threading import Lock
import topics_types.mqtt_topic as mqtt_topic

def test_string_type():
    """
    Testing Summation function
    """

    #inst = mqtt_base_topic.mqtt_base_topic()
    inst = mqtt_topic.mqtt_topic_ifd()
    inst.simulation.connected.set_payload("Hej")


    assert "Hej" == inst.simulation.connected.type_to_string()


    inst.simulation.connected.set_payload(1)


    assert "1" == inst.simulation.connected.type_to_string()

def test_bool_type():
    """
    Testing Summation function
    """

    #inst = mqtt_base_topic.mqtt_base_topic()
    inst = mqtt_topic.mqtt_topic_ifd()
    inst.simulation.started.set_payload(True)


    assert "True" == inst.simulation.started.type_to_string()


    inst.simulation.started.set_payload(False)


    assert "False" == inst.simulation.started.type_to_string()


    inst.simulation.started.set_payload(0)


    assert "False" == inst.simulation.started.type_to_string()

    inst.simulation.started.set_payload('False')


    assert "False" == inst.simulation.started.type_to_string()

def test_int_type():
    """
    Testing Summation function
    """

    #inst = mqtt_base_topic.mqtt_base_topic()
    inst = mqtt_topic.mqtt_topic_ifd()
    inst.simulation.speed.set_payload(12)
    assert "12" == inst.simulation.speed.type_to_string()


    inst.simulation.speed.set_payload("123.51")
    assert "124" == inst.simulation.speed.type_to_string()

    inst.simulation.speed.set_payload(123.49)
    assert "123" == inst.simulation.speed.type_to_string()

    inst.simulation.speed.set_payload(123.001)
    assert "123" == inst.simulation.speed.type_to_string()

    inst.simulation.speed.set_payload(123.99999)
    assert "124" == inst.simulation.speed.type_to_string()


    inst.simulation.speed.set_payload(True)


    assert "1" == inst.simulation.speed.type_to_string()

def test_datetime_type():
    """
    Testing Summation function
    """

    #inst = mqtt_base_topic.mqtt_base_topic()
    inst = mqtt_topic.mqtt_topic_ifd()
    inst.message.time_start.set_payload("2024-06-07 12:23:12.23")
    assert "2024-06-07 12:23:12.230000" == inst.message.time_start.type_to_string()

    inst.message.time_start.set_payload(inst.message.time_start.get_payload())
    assert "2024-06-07 12:23:12.230000" == inst.message.time_start.type_to_string()