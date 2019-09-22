import xml.dom.minidom

doc = xml.dom.minidom.parse("mqtt_topic.xml")
file = open("mqtt_topic.py", "w+")


def get_childnode(node):
    childs = []
    for n in node.childNodes:
        if type(n) == xml.dom.minidom.Element:
            childs.append(n.tagName)
    return childs


def parse_node(node, parent):
    for n in node.childNodes:
        if type(n) == xml.dom.minidom.Element:
            name = "{}{}".format(parent, n.tagName)
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
                file.write(
                    "        self.message_dictonary = message_dictonary\n")

            else:
                file.write(
                    "    def __init__(self, message_to_send, message_dictonary):\n")
                file.write("        self.message_to_send = message_to_send\n")
                file.write(
                    "        message_dictonary['{}'] = self\n".format(name))

            if parent != None:
                file.write("        self.topic = '{}'\n".format(name))
            childs = get_childnode(n)

            if len(childs) == 0:

                if n.getAttribute("message") != "":
                    file.write("        self.payload = None\n")
                    file.write("\n")
                    file.write("    def get_{}(self):\n".format(
                        n.getAttribute("message")))
                    file.write("        return {}(self.payload)\n".format(
                        n.getAttribute("type")))
                    file.write("\n")
                    file.write("    def set_{}(self, {}):\n".format(
                        n.getAttribute("message"), n.getAttribute("message")))
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
                    "        message_to_send = str(len(message_to_send)).rjust(\n")
                file.write("           3, '0') + message_to_send\n")

                file.write("        return message_to_send\n")
                file.write("\n")

                if n.getAttribute("message") == "":
                    file.write("    def publish(self):\n")
                    file.write("        message = ''\n")
                else:
                    file.write("    def publish(self, {}):\n".format(n.getAttribute(
                        "message")))
                    file.write("        message = {}\n".format(n.getAttribute(
                        "message")))
                file.write(
                    "        self.message_to_send.append(self.create_message(self.topic, message))\n")

                file.write("\n")

                file.write("    def subscribe(self):\n")
                file.write(
                    "        self.message_to_send.append(self.create_message('subscribe', self.topic))\n")

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
                file.write("        self.{} = mqtt_topic_{}(self.message_to_send, message_dictonary)\n".format(
                    child, child))
            file.write("\n")

            if parent == None:
                file.write("    def get_message_to_send(self):\n")
                file.write("        return self.message_to_send\n")

                file.write("    def clear_message_to_send(self):\n")
                file.write("        self.message_to_send = []\n")

                file.write("    def get_message(self, message_as_text):\n")
                file.write(
                    "        return self.message_dictonary[message_as_text]\n")

        file.write("\n")
        file.write("\n")


parse_node(doc, None)
file.close()
