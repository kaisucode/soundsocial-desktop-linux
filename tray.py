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

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()

