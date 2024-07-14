import plugins


class MQTT_BOOL(plugins.PluginHandler):

    def __init__(self):
        pass

    def get_type_to_string(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return "{}".format(self.payload)\n')
    
    def get_convert_to_type(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return bool(payload)\n')

class MQTT_INT(plugins.PluginHandler):

    def __init__(self):
        pass

    def get_type_to_string(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return "{}".format(self.payload)\n')
    
    def get_convert_to_type(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return int(float(payload)+0.5)\n')
    

class MQTT_DATETIME(plugins.PluginHandler):

    def __init__(self):
        pass

    def get_type_to_string(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return {}self.payload.strftime("%Y-%m-%d %H:%M:%S.%f")\n'.format(indent))     
    
    def get_convert_to_type(self, file, indent):
            file.write('{}'.format(indent))
            file.write('conerted = None\n')
            file.write('{}'.format(indent))
            file.write('if isinstance(payload, datetime):\n')
            file.write('{}'.format(indent))
            file.write('    conerted = payload\n')
            file.write('{}'.format(indent))
            file.write('elif isinstance(payload, str):\n')
            file.write('{}'.format(indent))
            file.write('    conerted = datetime.strptime(payload, "%Y-%m-%d %H:%M:%S.%f")\n')
            file.write('{}'.format(indent))
            file.write('return conerted')
    

class MQTT_STRING(plugins.PluginHandler):

    def __init__(self):
        pass

    def get_type_to_string(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return "{}".format(self.payload)\n')

    def get_convert_to_type(self, file, indent):
        file.write('{}'.format(indent))
        file.write('return "{}".format(payload)\n')
