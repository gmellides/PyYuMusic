import pygubu
import tkinter
import os
from graphics import NewPlaylist


class PlayListManagerWindow(pygubu.TkApplication):

    def  __init__(self, master):
        self.builder = builder = pygubu.Builder()
        form_path = os.path.join(os.path.dirname(__file__), "PlaylistManager.ui")
        builder.add_from_file(form_path)
        self.mainwindow = builder.get_object('mainFrame', master)
        builder.connect_callbacks(self)

    def btn_newPlaylist_action(self):
        tp = tkinter.Toplevel()
        tp.title("Playlist Manager")
        win = NewPlaylist.NewPlaylistForm(tp)
        tp.resizable(False, False)
        tp.mainloop()