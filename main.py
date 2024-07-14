from plugins import PluginHandler

if __name__ == '__main__':
    for p  in PluginHandler.plugins:
        inst = PluginHandler.plugins["MQTT_BOOL"]
        #print("INST: ", type(inst))
        inst.get_type_to_string()

