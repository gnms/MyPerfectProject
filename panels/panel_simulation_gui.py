
import tkinter
from threading import Thread


class panel_simulation_gui(Thread):
    def __init__(self, mqtt_client):
        Thread.__init__(self)
        self.mqtt_client = mqtt_client
        self.mqtt_client.mqtt_topic.environment.date_time.subscribe()

    def on_started(self):
        if self.started_btn.config('text')[-1] == 'start':
            self.mqtt_client.mqtt_topic.simulation.started.publish(True)
            self.started_btn.config(text='stop')
        else:
            self.mqtt_client.mqtt_topic.simulation.started.publish(False)
            self.started_btn.config(text='start')
        self.mqtt_client.send_message_to_server()

    def on_speed(self):
        self.mqtt_client.mqtt_topic.simulation.speed.publish(
            self.speed_inp.get())
        self.mqtt_client.send_message_to_server()

    def on_date_time(self):
        self.mqtt_client.mqtt_topic.environment.date_time.publish(self.date_time_inp.get())
        self.mqtt_client.send_message_to_server()

    def run(self):
        self.gui = tkinter.Tk()
        # Code to add widgets will go here...
        self.gui.title("panel_time")

        main_frame = tkinter.Frame(self.gui)
        main_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        simulation_frame = tkinter.LabelFrame(main_frame, text='simulation')
        simulation_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        self.started_btn = tkinter.Button(simulation_frame, text="start", command=self.on_started)
        self.started_btn.pack(side=tkinter.LEFT)

        speedframe = tkinter.Frame(simulation_frame)
        speedframe.pack(side=tkinter.LEFT)

        speed_lbl = tkinter.Label(speedframe, text="speed")
        speed_lbl.pack(side=tkinter.LEFT)
        self.speed_inp = tkinter.Entry(speedframe, text="100")
        self.speed_inp.pack(side=tkinter.LEFT)
        self.speed_is = tkinter.Label(speedframe, text="todo")
        self.speed_is.pack(side=tkinter.LEFT)
        speed_btn = tkinter.Button(speedframe, text="send", command=self.on_speed)
        speed_btn.pack(side=tkinter.LEFT)

        fillframe = tkinter.LabelFrame(simulation_frame, text='FILL')
        fillframe.pack(side=tkinter.RIGHT, fill=tkinter.X, expand=1)

        # environment
        environment_frame = tkinter.LabelFrame(main_frame, text='environment')
        environment_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        date_timeframe = tkinter.Frame(environment_frame)
        date_timeframe.pack(side=tkinter.LEFT)
        date_time_lbl = tkinter.Label(date_timeframe, text="date_time")
        date_time_lbl.pack(side=tkinter.LEFT)
        self.date_time_inp = tkinter.Entry(date_timeframe, text="date_time")
        self.date_time_inp.pack(side=tkinter.LEFT)
        self.date_time_is = tkinter.Label(date_timeframe, text="date_time")
        self.date_time_is.pack(side=tkinter.LEFT)
        date_time_btn = tkinter.Button(date_timeframe, text="send", command=self.on_date_time)
        date_time_btn.pack(side=tkinter.LEFT)

        fillframe = tkinter.LabelFrame(environment_frame, text='FILL')
        fillframe.pack(side=tkinter.RIGHT, fill=tkinter.X, expand=1)

        # clients
        client_frame = tkinter.LabelFrame(main_frame, text='clients')
        client_frame.pack(fill=tkinter.X, expand=1, anchor=tkinter.NW)

        self.client_list = tkinter.Listbox(client_frame)

        for existing_client in self.mqtt_client.online_client_list:
            self.client_list.insert(self.client_list.size() + 1, existing_client)
            self.mqtt_client._log.info('Add client {}'.format(existing_client))

        # self.client_list.insert(1, "Python")
        # self.client_list.insert(2, "Perl")
        self.client_list.pack(side=tkinter.LEFT)
        fillframe = tkinter.LabelFrame(client_frame, text='FILL')
        fillframe.pack(side=tkinter.RIGHT, fill=tkinter.X, expand=1)

        fillframe = tkinter.Frame(self.gui)
        fillframe.pack(fill=tkinter.BOTH, expand=1, anchor=tkinter.NW)

        self.gui.mainloop()

    def show_gui(self):
        self.start()


# if __name__ == '__main__':
#     panel_time_gui = panel_time_gui()

#     panel_time_gui.show_gui()
#     print("HEJ")
