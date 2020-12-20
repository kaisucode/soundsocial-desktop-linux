#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("Goodpods", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  command_one = gtk.MenuItem('Start recording')
  command_one.connect('activate', startRecording)
  menu.append(command_one)

  command_two = gtk.MenuItem('Stop recording')
  command_two.connect('activate', stopRecording)
  menu.append(command_two)

  exittray = gtk.MenuItem('Exit Tray')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def startRecording(_):
    print("start recording")

def stopRecording(_):
    print("stop recording")
    # input popup for title
    # send to server
    #  from .input import EntryWindow
    var1 = EntryWindow()
    var1.show()


def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Clip Title")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Submit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

        self.connect("destroy", lambda x: Gtk.main_quit())
        self.add(Gtk.Label("This is another window"))
        self.show_all()



    def on_close_clicked(self, button):
        print("Closing application")
        print(self.entry.get_text())
        subw = EntryWindow()
        Gtk.main_quit()


