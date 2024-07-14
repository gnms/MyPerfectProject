
import tkinter
from threading import Thread, Lock
from mqtt_base_topic import mqtt_leaf_topic


class panel_signal_mgr_gui(Thread):
    def __init__(self, mqtt_topic_ifd):
        Thread.__init__(self)
        self.nr_of_scripts = 0

        self.mqtt_topic = mqtt_topic_ifd

        # self.signal_list = []
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

        # xml_doc = xml.dom.minidom.parse("mqtt_topic.xml")

        # self.parse_xml(xml_doc, "", "")

        
        # signal = override_signal(parent_path)
        # self.signal_list.append(signal)
        # self.signal_dict[parent_path] = signal
        # print("name = {}".format(parent_path))

        index = 0
        for topic in self.mqtt_topic.get_all_leafs():
            if isinstance(topic, mqtt_leaf_topic):
                self.add_script(topic, index)   
                index = index + 1
        self.lock.release()

    def run(self):
        self.create_gui()
        self.gui.mainloop()

    def on_override(self, signal, override_btn, override_inp, update_btn):
        if override_btn.config('relief')[-1] == 'sunken':
            override_btn.config(relief="raised", text="Off")
            override_btn.config(bg="light gray")
            update_btn.config(state=tkinter.DISABLED)
            signal.override(False, "")
        else:
            override_btn.config(relief="sunken", text="On")
            override_btn.config(bg="white")
            update_btn.config(state=tkinter.NORMAL)
            signal.override(True, override_inp.get())

    def on_update(self, signal, override_inp):
        signal.override(True, override_inp.get())
        


    def on_send(self, signal):
        signal.publish()
        pass

    def add_script(self, signal, index):
        name = signal.get_topic()
        signal_frame = tkinter.Frame(self.main_frame)
        signal_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        signal_lbl = tkinter.Label(signal_frame, text=name)
        signal_lbl.pack(side=tkinter.LEFT)
        send_btn = tkinter.Button(signal_frame, text="Send", command=lambda: self.on_send(signal))
        send_btn.pack(side=tkinter.RIGHT)
        update_btn = tkinter.Button(signal_frame, text="Update", command=lambda: self.on_update(signal, override_inp))
        update_btn.config(state=tkinter.DISABLED)
        update_btn.pack(side=tkinter.RIGHT)
        override_inp = tkinter.Entry(signal_frame, text="input_{}".format(index), bg="light gray")
        override_btn = tkinter.Button(signal_frame, text="Off", command=lambda: self.on_override(signal, override_btn, override_inp, update_btn))
        override_btn.pack(side=tkinter.RIGHT)
        override_inp = tkinter.Entry(signal_frame, text="input_{}".format(index), bg="light gray")
        override_inp.pack(side=tkinter.RIGHT)

        # entry_text = tkinter.StringVar()
        signal_value = tkinter.Entry(signal_frame, text="value_{}".format(index), state="disable", disabledbackground="white")  # , textvariable=entry_text)
        signal_value.pack(side=tkinter.RIGHT)

        self.signal_dict[name] = signal_value

        #signal.set_button(override_btn, override_inp, signal_value)

    # def parse_xml(self, xml_doc, parent_path, sep):
    #     if xml_doc.childNodes.length > 0:
    #         for node in xml_doc.childNodes:
    #             if type(node) == xml.dom.minidom.Element:
    #                 if node.nodeName == "ifd":
    #                     self.parse_xml(node, "", "")
    #                     pass
    #                 else:
    #                     self.parse_xml(
    #                         node, "{}{}{}".format(parent_path, sep, node.nodeName), '/')
    #     else:
    #         signal = override_signal(parent_path)
    #         self.signal_list.append(signal)
    #         self.signal_dict[parent_path] = signal
    #         print("name = {}".format(parent_path))

    def show_gui(self):
        self.gui.mainloop()

    def update_date(self, topic, payload):
        self.lock.acquire(True)
        input = self.signal_dict[topic]
        input.config(state="normal")
        input.delete(0, tkinter.END)
        input.insert(0, payload)
        input.config(state="disable")
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

    # def get_send_message(self):
    #     all_message = None
    #     self.lock.acquire(True)
    #     for signal in self.signal_list:
    #         message = signal.get_override()
    #         if message != None:
    #             if all_message == None:
    #                 all_message = "{}".format(message)
    #             else:
    #                 all_message = "{},{}".format(all_message, message)

    #         if all_message != None and len(all_message) > 900:
    #             break

    #     self.lock.release()
    #     if all_message != None:
    #         all_message = "[{}]".format(all_message)
    #     return all_message


if __name__ == '__main__':
    panel_signal_mgr_gui = panel_signal_mgr_gui()

    panel_signal_mgr_gui.show_gui()
#     print("HEJ")
