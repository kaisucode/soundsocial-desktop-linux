import os
import signal
import time
import subprocess 
import requests
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator


APPINDICATOR_ID = 'soundsocial'
pipeline = "ffmpeg -f pulse -i default output.wav"
# change .wav to .mp3 to generate mp3 files instead

p = None

def main():
    indicator = appindicator.Indicator.new("SoundSocial", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
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
    global p
    p = subprocess.Popen(pipeline, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

def stopRecording(_):
    print("stop recording")
    global p
    p.communicate(input=b'q')
    p.terminate()
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
        clipTitle = self.entry.get_text()
        print("clip title: " + clipTitle)
        sendToServer(clipTitle)
        self.hide()

def sendToServer(clipTitle): 
    MONGO_ID = "5fde50a79f83059f957f781d"

    url = "http://10.0.0.172:5000/clip"
    data = {
        "mongo_id": MONGO_ID,
        "title": clipTitle, 
        "url": "#"
    }   
    files = {
        "file": open('output.wav', 'rb'),
    }

    r = requests.post(url, files=files, data=data)

    print(r.status_code, r.reason)
    print("POST request sent")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()

