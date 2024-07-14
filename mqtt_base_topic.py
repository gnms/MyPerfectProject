
from datetime import datetime

class mqtt_base_topic ():
    def __init__(self, message_to_send, message_dictonary, lock, topic):
        self.message_to_send = message_to_send
        self.message_dictonary = message_dictonary
        message_dictonary[topic] = self   
        self.topic = topic  
        self.lock = lock

    def get_message_to_send(self):
        return self.message_to_send

    def clear_message_to_send(self):
        self.message_to_send.clear()

    def get_message(self, message_as_text):
        return self.message_dictonary[message_as_text]
    
    def get_topic(self) -> str:
        return self.topic



class mqtt_leaf_topic (mqtt_base_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)
        self.payload = None

    def get_payload(self):
        return self.payload

    def set_payload(self, time):
        self.payload = self.convert_to_type(time)     
        print (self.payload)   
    
    def create_message(self, topic, message, retain=""):
        if isinstance(topic, str):
            topic_str = topic
        else:
            topic_str = topic.topic
        message_to_send = '{}:{}:{}'.format(topic_str, retain, message)
        if __debug__ == True:
            message_to_send = str(len(message_to_send.encode())).rjust(
               3, '0') + message_to_send
        return message_to_send

    def publish(self, topic_type=None):
        self.lock.acquire()
        if topic_type != None:
            self.set_payload(topic_type)
        message = self.type_to_string() 
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()   

      
    def override(self, override, value):
        if override == True:
            override_str = "override"
        else:
           override_str = "normal"
        payload = "{{\"name\": \"{}\",\"state\": \"{}\",\"value\": \"{}\" }}".format(
                self.topic, override_str, value)
        self.lock.acquire()
        self.message_to_send.append(self.create_message('override', payload))
        self.lock.release()

    def subscribe(self):
        self.lock.acquire()
        self.message_to_send.append(self.create_message('subscribe', self.topic))
        self.lock.release()
   
    def __eq__(self, other):
        if other == None:
            return False

        if type(other) is str:
            other_topic = other
        else:            
            other_topic = other.topic

        if self.topic == other_topic:
            return True
        else:
            return False
             

    def type_to_string(self):
        return ""
    

    def convert_to_type(self, payload):
        return
    
class mqtt_string_topic (mqtt_leaf_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        return "{}".format(payload)


    
class mqtt_int_topic (mqtt_leaf_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        return int(float(payload)+0.5)    
    

class mqtt_datetime_topic (mqtt_leaf_topic):
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
    

class mqtt_bool_topic (mqtt_leaf_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)

    def type_to_string(self):
        return "{}".format(self.payload)

    def convert_to_type(self, payload):
        if isinstance(payload, bool):
            return payload
        if payload == "True":
            return True
        return False
    

class mqtt_void_topic (mqtt_leaf_topic):
    def __init__(self, message_to_send, message_dictonary, lock, topic_name):
        super().__init__(message_to_send, message_dictonary, lock, topic_name)