import xml.dom.minidom
from parse_topics_types import get_all_topic_typed
import os


path = os.path.abspath(__file__)
search_directory = os.path.dirname(path)

# Parse the XML document
doc = xml.dom.minidom.parse(f"{search_directory}/mqtt_topic.xml")

# Open the output Python file for writing

file = open(f"{search_directory}/mqtt_topic.py", "w+")


def get_childnode(node):
    """
    Get all child elements of a given XML node.
    
    :param node: XML node
    :return: List of tag names of child elements
    """
    childs = []
    for n in node.childNodes:
        if isinstance(n, xml.dom.minidom.Element):
            childs.append(n.tagName)
    return childs


def print_subscribe_all(node, parent_name):
    """
    Recursively print subscribe statements for all child nodes.
    
    :param node: XML node
    :param parent_name: Parent node's name
    """
    for child in node.childNodes:
        if isinstance(child, xml.dom.minidom.Element):
            print_subscribe_all(child, f"{parent_name}.{child.tagName}")
            if len(get_childnode(child)) == 0:
                file.write(f"        self{parent_name}.{child.tagName}.subscribe()\n")

def print_all_leafs(node, parent_name):
    """
    Recursively print subscribe statements for all child nodes.
    
    :param node: XML node
    :param parent_name: Parent node's name
    """
    str = ""
    for child in node.childNodes:
        if isinstance(child, xml.dom.minidom.Element):
            if str == "":
                str = print_all_leafs(child, f"{parent_name}.{child.tagName}")
            else:
                    s = print_all_leafs(child, f'{parent_name}.{child.tagName}')
                    if s != "":
                        str = f"{str},\n{s}"
            if len(get_childnode(child)) == 0:
                if str == "":
                    str = f"self{parent_name}.{child.tagName}"
                else:
                    str = f"{str},\nself{parent_name}.{child.tagName}"
    return  str


def parse_leaf(node, parent):
    """
    Parse leaf nodes and write corresponding class attributes to file.
    
    :param node: XML node
    :param parent: Parent node's name
    """
    for n in node.childNodes:
        if isinstance(n, xml.dom.minidom.Element):
            if n.hasChildNodes():
                file.write(f"        self.{n.localName} = mqtt_topic_{n.localName}(self.message_to_send, self.message_dictonary, self.lock, '{parent}{n.localName}')\n")
            else:
                file.write(f"        self.{n.localName} = mqtt_{n.getAttribute('type')}_topic(self.message_to_send, self.message_dictonary, self.lock, '{parent}{n.localName}')\n")


def parse_node(node, parent):
    """
    Recursively parse XML nodes and write corresponding class definitions to file.
    
    :param node: XML node
    :param parent: Parent node's name
    """
    for n in node.childNodes:
        childs = get_childnode(n)
        if isinstance(n, xml.dom.minidom.Element):
            # Determine the node's name based on its parent
            if parent is None:
                name = ""
                parse_node(n, "")
            else:
                if parent == "":
                    name = f"{n.tagName}"
                else:
                    name = f"{parent}/{n.tagName}"
                
                parse_node(n, f"{name}")

            # Write class definition for the node
            if parent is None:
                file.write(f"\nclass mqtt_topic_{n.tagName} (mqtt_base_topic):\n")
                file.write("    def __init__(self):\n")
                file.write("        super().__init__([], dict(), Lock(), \"\")\n")
            else:
                if len(childs) > 0:
                    file.write(f"\nclass mqtt_topic_{n.tagName} (mqtt_base_topic):\n")
                    file.write("    def __init__(self, message_to_send, message_dictonary, lock, topic_name):\n")
                    file.write("        super().__init__(message_to_send, message_dictonary, lock, topic_name)\n")

            # Parse the leaf nodes of the current node
            if parent is None:
                parse_leaf(n, "")
            else:
                parse_leaf(n, f"{name}/")

            # Add methods to the root class
            if parent is None:
                file.write("    def subscribe_all(self):\n")
                print_subscribe_all(n, "")
                file.write("    def get_all_leafs(self):\n")
                file.write(f"        return [{print_all_leafs(n, "")}]\n")
                


# Write the necessary imports to the output file
file.write("from threading import Lock\n")
file.write("from topics_types.mqtt_base_topic import mqtt_base_topic")

# Get all topic types and write them as imports
all_types = get_all_topic_typed()
for subclass in all_types:
    file.write(f", {subclass.__name__}")

# Parse the XML document starting from the root
parse_node(doc, None)

# Close the output file
file.close()