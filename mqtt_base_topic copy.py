
class mqtt_base_topic ():
    def __init__(self, message_to_send, message_dictonary, lock, topic):
        self.message_to_send = message_to_send
        self.message_dictonary = message_dictonary
        message_dictonary[topic] = self   
        self.topic = topic  
        self.lock = lock
        self.payload = None

    def get_payload(self):
        return self.string_to_type()    

    def set_payload(self, time):
        self.payload = time    
    
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

    def publish(self, topic_type):
        self.lock.acquire()
        message = self.type_to_string(topic_type) 
        self.message_to_send.append(self.create_message(self.topic, message))
        self.lock.release()   

    def publish(self):
        self.lock.acquire()
        message = ""
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
    

    def string_to_type(self):
        return