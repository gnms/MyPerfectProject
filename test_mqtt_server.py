from server.mqtt_server import mqtt_server


def test_mqtt_split_msg():
    msg = "kalle:pelle:sture"
    delemiter = msg.find(":")
    topic = msg[:delemiter]


def test_override_parese():
    server = mqtt_server('', 12345)
    msg = "[{\"name\":\"simulation/started\",\"state\":\"override\",\"value\":\"\"},{\"name\":\"simulation/speed\",\"state\":\"override\",\"value\":\"\"},{\"name\":\"simulation/override\",\"state\":\"override\",\"value\":\"\"},{\"name\":\"environment/date_time\",\"state\":\"override\",\"value\":\"\"},{\"name\":\"environment/is_dark_outside\",\"state\":\"override\",\"value\":\"\"}]"
    server.parse_override(msg)

    msg = "[{\"name\":\"simulation/started\",\"state\":\"normal\",\"value\":\"\"},{\"name\":\"simulation/override\",\"state\":\"normal\",\"value\":\"\"},{\"name\":\"environment/is_dark_outside\",\"state\":\"normal\",\"value\":\"\"}]"
    server.parse_override(msg)
