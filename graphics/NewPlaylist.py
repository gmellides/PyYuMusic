import pygubu
import os
import tkinter
from tkinter import messagebox as msg
from utilities import metadata as info
from utilities import playlist_writer

songlist = None
songURLs = None
writer = playlist_writer.PlaylistCreator()

"""
    Name: add_songInfo_list
    Type: Method
    Description: Adds a row on table with the song title and the duration
"""
def add_songInfo_list(name,duration):
    songlist.insert('', tkinter.END, text=name, values=duration)


class NewPlaylistForm:

    def __init__(self, master):
        global songlist
        global songURLs
        global writer
        self.builder = builder = pygubu.Builder()
        form_path = os.path.join(os.path.dirname(__file__), 'NewPlaylist.ui')
        builder.add_from_file(form_path)
        self.mainwindow = builder.get_object('mainFrame', master)
        builder.connect_callbacks(self)
        songlist = self.builder.get_object('lst_songs')

    def btn_savePlaylist_action(self):
        txt_name = self.builder.get_object('txt_playlistName')
        if not len(txt_name.get()) == 0:
            if playlist_writer.PlaylistCreator.namePlaylist(self, txt_name.get()):
                playlist_writer.PlaylistCreator.save_playlist(self)
                msg.showinfo("Success", "Your playlist is ready")
        else:
           msg.showerror("Error", "Error message")

    def btn_addSong_action(self):
        txt_url = self.builder.get_object('txt_url')
        youtube_url = txt_url.get()
        # Adds the song url to playlist xml file
        playlist_writer.PlaylistCreator.add_song_to_playlist(self, youtube_url)
        # Adds song info to table
        add_songInfo_list(info.SongInfo.get_song_title(self, youtube_url), info.SongInfo.get_song_duration(self))
        # Clears the url box
        txt_url.delete(0, 'end')