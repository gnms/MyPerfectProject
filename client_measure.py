from clients.mqtt_client import mqtt_client


class client_measure(mqtt_client):
    '''Returned argument a is squared.'''
    def __init__(self):
        mqtt_client.__init__(self, self.__class__.__name__)

    

    def io_ten_yard(self, digital_io):
        pass

    def io_twenty_yard(self, digital_io):
        pass

    def io_thirty_yard(self, digital_io):
        pass

    def io_fourty_yard(self, digital_io):
        pass

    def io_time_start(self, digital_io):
        pass
    

    def message_reset_value(self, value):
        pass

    def message_reset_counter(self, value):
        pass



if __name__ == '__main__':
    client_measure = client_measure()
    
    client_measure.run()
