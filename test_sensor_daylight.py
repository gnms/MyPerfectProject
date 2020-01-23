from sensor_daylight import sensor_daylight


def test_daylight_model():
    client = sensor_daylight()
    assert 896 == client.get_light_from_sun_angle(10)
    assert 290123.6 == client.get_light_from_sun_angle(0)
    assert 532705.2 == client.get_light_from_sun_angle(-2)
    assert 706429 == client.get_light_from_sun_angle(-24)
    # assert client.active_clients["KALLE"] == CLIENT_STATES.IDLE
