class mqtt_string_topic (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        return "{}".format(payload)


    
class mqtt_int_topic (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        return int(float(payload)+0.5)    
    

class mqtt_datetime_topic (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return         self.payload.strftime("%Y-%m-%d %H:%M:%S.%f")

    def convert_to_type(self, payload):
        conerted = None
        if isinstance(payload, datetime):
            conerted = payload
        elif isinstance(payload, str):
            conerted = datetime.strptime(payload, "%Y-%m-%d %H:%M:%S.%f")
        return conerted
    

class mqtt_bool_topic (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        return bool(payload)