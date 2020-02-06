
import tkinter
from threading import Thread
from mqtt_topic import string_to_time
import subprocess
import xml.dom.minidom


class script_data():
    def __init__(self, button, path, auto_start):
        self.button = button
        self.path = path
        self.proc = None
        self.button.config(bg='red')
        self.button.config(activebackground='red')
        self.button.config(text='Start')
        self.auto_start = auto_start

    def toogle_script(self):
        if self.proc == None:
            # start script
            self.proc = subprocess.Popen(["python3", "{}".format(self.path)])
        else:
            # stop script
            self.proc.kill()
            self.proc = None

    def check_if_alive(self):
        if self.proc != None and self.proc.poll() == None:
            self.button.config(bg='green')
            self.button.config(activebackground='green')
            self.button.config(text='Stop')
        else:
            self.button.config(bg='red')
            self.button.config(activebackground='red')
            self.button.config(text='Start')
            self.proc = None

    def exit_script(self):
        if self.proc != None:
            self.proc.kill()
            self.proc = None

    def start_on_start(self):
        if self.auto_start:
            self.toogle_script()


class panel_start_mgr():
    def __init__(self):
        self.gui = tkinter.Tk()
        self.script_list = []
        self.nr_of_scripts = 0

        self.gui.title("Start manager")

        self.gui.protocol("WM_DELETE_WINDOW", self.on_close)

        main_frame = tkinter.Frame(self.gui)
        main_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        self.simulation_frame = tkinter.LabelFrame(main_frame, text='Scripts')
        self.simulation_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        script_frame = tkinter.Frame(self.simulation_frame)
        script_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        xml_doc = xml.dom.minidom.parse("start_mgr.xml")

        root = self.find_root(xml_doc)
        self.parse_file(root)

        # start if auto

        for script in self.script_list:
            script.start_on_start()

        self.check_proceses()

    def on_close(self):
        for script in self.script_list:
            script.exit_script()
        self.gui.destroy()

    def find_root(self, doc):
        for n in doc.childNodes:
            if type(n) == xml.dom.minidom.Element:
                if n.tagName == "scripts":
                    return n
        return None

    def parse_file(self, root):
        for node in root.childNodes:
            if type(node) == xml.dom.minidom.Element:
                self.add_script(node.getAttribute(
                    "name"), node.getAttribute("path"), node.getAttribute("auto_start"))

    def on_started(self, nr):
        self.script_list[nr].toogle_script()
        print("")
        pass

    def add_script(self, name, path, auto_start):
        script_frame = tkinter.Frame(self.simulation_frame)
        script_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        speed_lbl = tkinter.Label(
            script_frame, text=name)
        speed_lbl.pack(side=tkinter.LEFT)
        index = self.nr_of_scripts
        self.started_btn = tkinter.Button(
            script_frame, text="start", command=lambda: self.on_started(index))
        self.started_btn.pack(side=tkinter.RIGHT)

        self.script_list.append(script_data(
            self.started_btn, path, auto_start))
        self.nr_of_scripts = self.nr_of_scripts + 1

    def show_gui(self):
        self.gui.mainloop()

    def check_proceses(self):
        for script in self.script_list:
            script.check_if_alive()
        self.gui.after(1000, self.check_proceses)


if __name__ == '__main__':
    panel_start_mgr = panel_start_mgr()

    panel_start_mgr.show_gui()
#     print("HEJ")
