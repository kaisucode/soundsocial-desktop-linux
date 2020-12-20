
#  gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AnotherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GCT")
        self.connect("destroy", lambda x: Gtk.main_quit())

        self.entry.set_text("Clip Title")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Submit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_close_clicked(self, button):
        print("Closing application")
        print(self.entry.get_text())
        Gtk.main_quit()




class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GCT")
        self.connect("destroy", lambda x: Gtk.main_quit())

        self.box = Gtk.Box()
        self.set_default_size(300, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.table = Gtk.Table(6, 5)

        self.button = Gtk.Button("sub-window")
        self.button.connect("clicked", self.open_window)
        self.table.attach(self.button, 0, 2, 0, 1)

        self.box.add(self.table)
        self.add(self.box)

        self.add(Gtk.Label("This is another window"))
        self.show_all()
        self.set_size_request(200, 100)

        self.timeout_id = None


    def open_window(self, win):
        subw = AnotherWindow()


def main():
    m = Main()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()

