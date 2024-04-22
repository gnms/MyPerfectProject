import xml.dom.minidom

doc = xml.dom.minidom.parse("mqtt_topic.xml")
file = open("mqtt_topic.py", "w+")


def get_childnode(node):
    childs = []
    for n in node.childNodes:
        if type(n) == xml.dom.minidom.Element:
            childs.append(n.tagName)
    return childs


def print_subscribe_all(node, parent_name):
    for child in node.childNodes:
        if type(child) == xml.dom.minidom.Element:
            print_subscribe_all(child, "{}.{}".format(
                parent_name, child.tagName))
            if len(get_childnode(child)) == 0:
                file.write("        self{}.{}.subscribe()\n".format(
                    parent_name, child.tagName))


def parse_node(node, parent):
    # Go through all childs in tree
    for n in node.childNodes:
        if type(n) == xml.dom.minidom.Element:
            name = "{}{}".format(parent, n.tagName)
            # Check if it is root for ifd or not
            if parent == None:
                name = "{}{}".format(parent, n.tagName)
                parse_node(n, "")
            else:
                name = "{}{}".format(parent, n.tagName)
                parse_node(n, "{}/".format(name))

            file.write("class mqtt_topic_{}:\n".format(n.tagName))
            if parent == None:
                file.write("    def __init__(self):\n")
                file.write("        self.message_to_send = []\n")
                file.write("        message_dictonary = dict()\n")
                file.write("        lock = Lock()\n")
                file.write(
                    "        self.message_dictonary = message_dictonary\n")

            else:
                file.write(
                    "    def __init__(self, message_to_send, message_dictonary, lock):\n")
                file.write("        self.message_to_send = message_to_send\n")
                file.write(
                    "        message_dictonary['{}'] = self\n".format(name))
                file.write("        self.topic = '{}'\n".format(name))

            file.write("        self.lock = lock\n")

            childs = get_childnode(n)

            if len(childs) == 0:

                if n.getAttribute("message") != "":
                    file.write("        self.payload = None\n")
                    file.write("\n")
                    file.write("    def get_payload(self):\n")
                    converter_from_string = ""
                    if n.getAttribute("type") == "bool":
                        converter_from_string = "'True' in"
                    elif n.getAttribute("type") == "date_time":
                        converter_from_string = "string_to_time"
                    elif n.getAttribute("type") == "int":
                        converter_from_string = "int"
                    elif n.getAttribute("type") == "float":
                        converter_from_string = "float"

                    file.write("        return {}(self.payload)\n".format(
                        converter_from_string))
                    file.write("\n")
                    file.write("    def set_payload(self, {}):\n".format(
                        n.getAttribute("message")))
                    file.write("        self.payload = {}\n".format(
                        n.getAttribute("message")))

                file.write("\n")

                file.write("    def create_message(self, topic, message):\n")
                file.write("        if isinstance(topic, str):\n")
                file.write("            topic_str = topic\n")
                file.write("        else:\n")
                file.write("            topic_str = topic.topic\n")

                file.write(
                    "        message_to_send = '{}:{}'.format(topic_str, message)\n")
                file.write(
                    "        if __debug__ == True:\n")
                file.write(
                    "            message_to_send = str(len(message_to_send.encode())).rjust(\n")
                file.write("               3, '0') + message_to_send\n")

                file.write("        return message_to_send\n")

                file.write("\n")

                if n.getAttribute("message") == "":
                    file.write("    def publish(self):\n")
                    file.write("        self.lock.acquire()\n")
                    file.write("        message = ''\n")
                else:
                    file.write("    def publish(self, {}):\n".format(n.getAttribute(
                        "message")))
                    file.write("        self.lock.acquire()\n")
                    convert_to_string = ""
                    if n.getAttribute("type") == "date_time":
                        convert_to_string = "time_to_string"
                    file.write("        message = {}({})\n".format(convert_to_string, n.getAttribute(
                        "message")))
                file.write(
                    "        self.message_to_send.append(self.create_message(self.topic, message))\n")
                file.write("        self.lock.release()\n")

                file.write("\n")

                file.write("    def subscribe(self):\n")
                file.write("        self.lock.acquire()\n")
                file.write(
                    "        self.message_to_send.append(self.create_message('subscribe', self.topic))\n")
                file.write("        self.lock.release()\n")

                file.write("    def __eq__(self, other):\n")
                file.write("        if other == None:\n")
                file.write("            return False\n")
                file.write("\n")
                file.write("        if type(other) is str:\n")
                file.write("            other_topic = other\n")
                file.write("        else:")
                file.write("            other_topic = other.topic\n")
                file.write("\n")
                file.write("        if self.topic == other_topic:\n")
                file.write("            return True\n")
                file.write("        else:\n")
                file.write("            return False\n")

            for child in childs:
                file.write("        self.{} = mqtt_topic_{}(self.message_to_send, message_dictonary, self.lock)\n".format(
                    child, child))
            file.write("\n")

            if parent == None:

                file.write("    def subscribe_all(self):\n")

                print_subscribe_all(n, "")

                file.write("\n")
                file.write("    def get_message_to_send(self):\n")
                file.write("        return self.message_to_send\n")

                file.write("    def clear_message_to_send(self):\n")
                file.write("        self.message_to_send.clear()\n")

                file.write("    def get_message(self, message_as_text):\n")
                file.write(
                    "        return self.message_dictonary[message_as_text]\n")

        file.write("\n")
        file.write("\n")


file.write("from datetime import datetime\n")
file.write("from threading import Lock\n")
file.write("def string_to_time(timeStr):\n")
file.write("    return datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')\n")


file.write("def time_to_string(_time):\n")
file.write("    return _time.strftime('%Y-%m-%d %H:%M:%S.%f')\n")

parse_node(doc, None)
file.close()
