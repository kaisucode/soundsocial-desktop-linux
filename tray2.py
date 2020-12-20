
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

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()

