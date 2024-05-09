# Panel Signal manager
Panel signal manager is amodul that subscribe in all signals in the messages, than it create a GUI there all signal i added.
From teh GUI it is possibly to see the sigla value but also overrid the signal with a new value.
It is also posibly to send the overriden value from the GUI.

When a signal is overriden the mqtt_server will replace the value of the message with the overriden value from the panel_signal_mgr GUI.
But if no one send a value you can push send button on the GUI to make the panel send the overriden value.


![](./pane_signal_mgr.drawio.svg)
