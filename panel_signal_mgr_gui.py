
import tkinter
from threading import Thread, Lock
from mqtt_topic import string_to_time
import subprocess
import xml.dom.minidom


class override_signal():
    def __init__(self, name):
        self.button = None
        self.signa_name = name
        self.input = None
        self.current_value = ""
        self.override_value = ""
        self.is_dirty = False  # To know when to send data to server
        self.to_send = False  # To know when to publish data

    def get_name(self):
        return self.signa_name

    def set_button(self, button, input, value):
        self.button = button
        self.input = input
        self.current_value = value

    def toogle(self):
        if self.button.config('relief')[-1] == 'sunken':
            self.button.config(relief="raised", text="Off")
            self.input.config(bg="light gray")
        else:
            self.button.config(relief="sunken", text="On")
            self.input.config(bg="white")

        self.is_dirty = True

    def set_payload(self, payload):
        self.current_value.config(state="normal")
        self.current_value.delete(0, tkinter.END)
        self.current_value.insert(0, "{}".format(payload))
        self.current_value.config(state="disable")

    def get_override(self):
        payload = None
        if self.is_dirty and self.button.config('text')[-1] == 'Off':
            payload = "{{\"name\": \"{}\",\"state\": \"{}\",\"value\": \"{}\" }}".format(
                self.signa_name, "normal", self.input.get())
        if self.is_dirty and self.button.config('text')[-1] == 'On':
            payload = "{{\"name\": \"{}\",\"state\": \"{}\",\"value\": \"{}\" }}".format(
                self.signa_name, "override", self.input.get())

        self.is_dirty = False

        return payload

    def update_value(self):
        self.is_dirty = True

    
    def send_value(self):
        self.to_send = True


class panel_signal_mgr_gui(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.nr_of_scripts = 0

        self.signal_list = []
        self.signal_dict = dict()
        self.lock = Lock()

    def create_gui(self):
        self.lock.acquire(True)
        self.gui = tkinter.Tk()
        self.gui.title("Signal manager")

        main_frame = tkinter.Frame(self.gui)
        main_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        self.main_frame = tkinter.LabelFrame(main_frame, text='Signals')
        self.main_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        signal_frame = tkinter.Frame(self.main_frame)
        signal_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        xml_doc = xml.dom.minidom.parse("mqtt_topic.xml")

        self.parse_xml(xml_doc, "", "")

        index = 0
        for signal in self.signal_list:
            self.add_script(signal, index)
            index = index + 1
        self.lock.release()

    def run(self):
        self.create_gui()
        self.gui.mainloop()

    def on_override(self, index):
        self.signal_list[index].toogle()
        pass

    def on_update(self, index):
        self.signal_list[index].update_value()
        pass


    def on_send(self, index):
        self.signal_list[index].send_value()
        pass

    def add_script(self, signal, index):
        name = signal.get_name()
        signal_frame = tkinter.Frame(self.main_frame)
        signal_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        signal_lbl = tkinter.Label(
            signal_frame, text=name)
        signal_lbl.pack(side=tkinter.LEFT)
        send_btn = tkinter.Button(
            signal_frame, text="Send", command=lambda: self.on_send(index))
        send_btn.pack(side=tkinter.RIGHT)
        update_btn = tkinter.Button(
            signal_frame, text="Update", command=lambda: self.on_update(index))
        update_btn.pack(side=tkinter.RIGHT)
        override_btn = tkinter.Button(
            signal_frame, text="Off", command=lambda: self.on_override(index))
        override_btn.pack(side=tkinter.RIGHT)
        override_inp = tkinter.Entry(
            signal_frame, text="input_{}".format(index), bg="light gray")
        override_inp.pack(side=tkinter.RIGHT)

        # entry_text = tkinter.StringVar()
        signal_value = tkinter.Entry(
            signal_frame, text="value_{}".format(index), state="disable", disabledbackground="white")  # , textvariable=entry_text)
        signal_value.pack(side=tkinter.RIGHT)

        signal.set_button(override_btn, override_inp, signal_value)

    def parse_xml(self, xml_doc, parent_path, sep):
        if xml_doc.childNodes.length > 0:
            for node in xml_doc.childNodes:
                if type(node) == xml.dom.minidom.Element:
                    if node.nodeName == "ifd":
                        self.parse_xml(node, "", "")
                        pass
                    else:
                        self.parse_xml(
                            node, "{}{}{}".format(parent_path, sep, node.nodeName), '/')
        else:
            signal = override_signal(parent_path)
            self.signal_list.append(signal)
            self.signal_dict[parent_path] = signal
            print("name = {}".format(parent_path))

    def show_gui(self):
        self.gui.mainloop()

    def update_date(self, topic, payload):
        self.lock.acquire(True)
        self.signal_dict[topic].set_payload(payload)
        self.lock.release()

    def get_override(self):
        all_message = None
        self.lock.acquire(True)
        for signal in self.signal_list:
            message = signal.get_override()
            if message != None:
                if all_message == None:
                    all_message = "{}".format(message)
                else:
                    all_message = "{},{}".format(all_message, message)

            if all_message != None and len(all_message) > 900:
                break

        self.lock.release()
        if all_message != None:
            all_message = "[{}]".format(all_message)
        return all_message

    def get_send_message(self):
        all_message = None
        self.lock.acquire(True)
        for signal in self.signal_list:
            message = signal.get_override()
            if message != None:
                if all_message == None:
                    all_message = "{}".format(message)
                else:
                    all_message = "{},{}".format(all_message, message)

            if all_message != None and len(all_message) > 900:
                break

        self.lock.release()
        if all_message != None:
            all_message = "[{}]".format(all_message)
        return all_message


if __name__ == '__main__':
    panel_signal_mgr_gui = panel_signal_mgr_gui()

    panel_signal_mgr_gui.show_gui()
#     print("HEJ")
