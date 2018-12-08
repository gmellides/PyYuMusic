import pygubu
import os
import tkinter
import time
from threading import Thread
from utilities import player
from utilities import metadata
from utilities import playlist_parser
from graphics import PlaylistManager

songlist = []
"""
    Name: init_appComponents
    Type: Method
    Description: Initialize application components
"""
def init_appComponents(self):
    global media_control
    global MediaThread
    global DurationThread
    global song_progressBar
    global _self
    global songlist
    _self = self
    # Media Control Object of Media Player Class
    media_control = player.MediaPlayer()
    # Thread Decleration for Media Player and Duration Counter
    MediaThread = Thread(target=media_worker, args=[self])
    DurationThread = Thread(target=current_duration_update, args=[])
    # Progress Bar Global variable init
    song_progressBar = self.builder.get_object('prg_songprogress')
    # normal || disable options
    control_buttons_toggle(self, 'disable')

# ----- Thread Workers -----
def media_worker(self):
    #media_control.PlaySelectedPlaylist(songlist)
    media_control.Play(media=media_control.prepare_media("https://www.youtube.com/watch?v=eZuB5TWrSv4"))
    # Changes the Song Title Label on Player Window
    currentSong_info_update(self, "https://www.youtube.com/watch?v=eZuB5TWrSv4")
    nextSong_title_update(self, "https://www.youtube.com/watch?v=LC4VJhn0SnQ&app=desktop")

"""
    Name: current_duration_update
    Type: Method
    Description: - Runs on a Thread -  This methods updates 
    the duration label placed in form.
"""
def current_duration_update():
    lbl_current = _self.builder.get_object('lbl_currentDuration')
    while True:
        lbl_current.configure(text=player.MediaPlayer.get_playedTime(_self))
        song_progressBar["value"] = player.MediaPlayer.get_playedTime_ms(_self)
        time.sleep(1)

# --------------------------

# ----- S -----
def init_playlist():
    """
        TODO: Playlst will be presented as "My playlist - name.glst"
        selected playlist will return the youtube urls as array
        and will be
    :return:
    """
    cmb_playlist = _self.builder.get_object('cmb_playlist')
    cmb_playlist['values'] = os.listdir(os.path.abspath(os.chdir("pls_files")))
    cmb_playlist.bind("<<ComboboxSelected>>", cmb_evt_listener)


# --------------------------
"""
    Name: cmb_evt_listener
    Type: Method
    Description: Used as an event for Playlist Combobox on Select event
    calls the control button toggle method to enable control buttons.
"""
def cmb_evt_listener(self):
    control_buttons_toggle(_self, 'normal')
    cmb_playlist = _self.builder.get_object('cmb_playlist')
    songlist = playlist_parser.PlaylistParser(cmb_playlist.get()).get_song_list()
    print(songlist)


def currentSong_info_update(self, url):
    lbl_songtitle = self.builder.get_object('lbl_songTitle')
    lbl_songDuration = self.builder.get_object('lbl_duration')
    lbl_songtitle.configure(text=metadata.SongInfo.get_song_title(self, url))
    lbl_songDuration.configure(text=metadata.SongInfo.get_song_duration(self))
    song_progressBar["maximum"] = player.MediaPlayer.get_songDuration_ms(self)

def nextSong_title_update(self, nextSong_url):
    lbl_nextSong = self.builder.get_object('lbl_nextSong')
    lbl_nextSong.configure(text=metadata.SongInfo.get_song_title(self, nextSong_url))

"""
    Name: control_button_toggle
    Type: Method
    Description: It Changes the state of Control Buttons 
"""
def control_buttons_toggle(self, new_state):
    btn_previous = self.builder.get_object('btn_previous')
    btn_previous['state'] = new_state
    btn_play = self.builder.get_object('btn_PlayPause')
    btn_play['state'] = new_state
    btn_next = self.builder.get_object('btn_next')
    btn_next['state'] = new_state
    btn_stop = self.builder.get_object('btn_stop')
    btn_stop['state'] = new_state


class PlayerForm(pygubu.TkApplication):

    """
        Init Player Window
        Description: Loads the ui file with components and links the callbacks
        from Gui to Code and Events.
    """
    def __init__(self, master):
        global Playlists_cmbItems
        # initializes the window and connects the callbacks
        self.builder = builder = pygubu.Builder()
        form_path = os.path.join(os.path.dirname(__file__), "PlayerWindow.ui")
        builder.add_from_file(form_path)
        self.mainwindow = builder.get_object('mainFrame', master)
        builder.connect_callbacks(self)
        #
        init_appComponents(self)
        # Assing list with xml files placed in pls_files folder
        init_playlist()
        self.PlayingFlag = True

    """
        Call Backs
        Description: There is a method for all Buttons placed on form.    
    """
    def btn_playPause_action(self):
        """
            Checks a boolean variable named Flag
             if it's true then the play method from media control will be called.
             if it's false then it means that a song is already playing and it pause
             it.
        :return:
        """
        # Take Playlist
        if self.PlayingFlag:
            # Starts the Thread with the media player
            MediaThread.start()
            DurationThread.start()
            self.PlayingFlag = False
        else:
            media_control.Pause()

    def btn_stop_action(self):
        self.PlayingFlag = True
        media_control.Stop()
        MediaThread.join(None)

    def btn_next_action(self):
        media_control.Stop()
        media_control.Play()

    def btn_previous_action(self):
        media_control.Stop()
        media_control.Play(self, "previous url")

    def btn_close_action(self):
        DurationThread.join(1)
        media_control.join(None)

    """
        Name: btn_editPlaylist_action
        Type: Method
        Description: Opens the Playlist Manager window 
    """
    def btn_editPlaylist_action(self):
        tp = tkinter.Toplevel()
        tp.title("Playlist Manager")
        app = PlaylistManager.PlayListManagerWindow(tp)
        tp.resizable(False, False)
        tp.mainloop()