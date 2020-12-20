
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator


d = gtk.Dialog()
d.add_buttons(gtk.STOCK_YES, 1, gtk.STOCK_NO, 2)

label = gtk.Label('Do you like GTK?')
label.show()
d.vbox.pack_start(label)

answer = d.run()
d.destroy()

print(answer)
