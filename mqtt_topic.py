class mqtt_topic_base:
    def __init__(self, topic_name, parent):
        self.topic_name = topic_name
        self.parent = parent

    def get_topic(self):
        if self.parent != None:
            return self.parent.get_topic() + "/" + self.topic_name
        else:
            return self.topic_name

    def __eq__(self, other):
        if other == None:
            return False
        self_topic = self.get_topic()

        if type(other) is str:
            other_topic = other
        else:
            other_topic = other.get_topic()

        if(self_topic == other_topic):
            return True
        else:
            return False


class mqtt_topic_leaf(mqtt_topic_base):
    def __init__(self, topic_name, parent):
        mqtt_topic_base.__init__(self, topic_name, parent)
        self.value = 0


class mqtt_topic_simulation(mqtt_topic_base):
    def __init__(self):
        mqtt_topic_base.__init__(self, "simulation", None)
        # Called when client started
        self.started = mqtt_topic_leaf("started", self)
        # Called by the client each time everyting is done and waiting for next time.
        self.idle = mqtt_topic_leaf("idle", self)
        # Requset from timemodell to tell all nodes to send started again
        self.verbose = mqtt_topic_leaf("verbose", self)


class mqtt_topic_environment(mqtt_topic_base):
    def __init__(self):
        mqtt_topic_base.__init__(self, "environment", None)
        # Called each time all clients shall execute one tick
        self.date_time = mqtt_topic_leaf("date_time", self)


class mqtt_topic:
    def __init__(self):
        self.simulation = mqtt_topic_simulation()
        self.environment = mqtt_topic_environment()
