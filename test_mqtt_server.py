
def test_mqtt_split_msg():
    msg = "kalle:pelle:sture"
    delemiter = msg.find(":")
    topic = msg[:delemiter]
