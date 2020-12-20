
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new("Goodpods", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    command_one = gtk.MenuItem('Start recording')
    command_one.connect('activate', startRecording)
    menu.append(command_one)

    command_two = gtk.MenuItem('Stop recording')
    command_two.connect('activate', stopRecording)
    menu.append(command_two)


    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def startRecording(_):
    print("start recording")

def stopRecording(_):
    print("stop recording")
    # input popup for title
    var1 = InputWindow()

def quit(source):
    gtk.main_quit()

class InputWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="GCT")
        self.set_size_request(400, 200)
        self.connect("destroy", lambda x: gtk.main_quit())


        vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = gtk.Entry()
        self.entry.set_text("Clip Title")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button = gtk.Button.new_with_mnemonic("Submit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)


        self.show_all()

    def on_close_clicked(self, button):
        print("Closing application")
        print(self.entry.get_text())
        gtk.main_quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()

