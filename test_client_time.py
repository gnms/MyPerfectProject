from clients.client_time import client_time
from clients.client_time import CLIENT_STATES


def test_mqtt_topic():
    client = client_time()
    client.add_active_client("KALLE")
    assert len(client.active_clients) == 1
    assert client.active_clients["KALLE"] == CLIENT_STATES.IDLE

    client.add_active_client("KALLE")
    assert len(client.active_clients) == 1

    client.add_active_client("PELLE")
    assert len(client.active_clients) == 2
    assert client.active_clients["PELLE"] == CLIENT_STATES.IDLE

    client.delete_active_client("PELLE")
    assert len(client.active_clients) == 1
    assert client.active_clients["KALLE"] == CLIENT_STATES.IDLE
