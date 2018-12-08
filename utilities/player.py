import pafy
import vlc
import time
from utilities import dconverter

vlc_player = None


class MediaPlayer:

    def __init__(self):
        global vlc_player
        global Instance
        Instance = vlc.Instance()
        vlc_player = Instance.media_player_new()

    """
        Name: Play
        Type: Class Method
        Parameter: Self and url
        Description: It takes as a parameter a youtube url 
    """
    def Play(self, media):
        Media = Instance.media_new(media)
        Media.get_mrl()
        vlc_player.set_media(Media)
        vlc_player.play()

    """
        Name: url_resolver
        Parameter: url - Youtube video URL 
        Description: Using Pafy 
    """
    def prepare_media(self, url):
        youtube_video = pafy.new(url)
        audio = youtube_video.getbestaudio()
        return audio.url


    """
        Name: 
        Type: 
        Description: 
    """
    def Stop(self):
        vlc_player.stop()

    """
        Name: 
        Type: 
        Description: 
    """
    def Pause(self):
        vlc_player.pause()

    """
        Name: 
        Type: 
        Description: 

    def change_song(self, newSong):
        vlc_player.stop()
        self.Play(self, newSong)
    """

    """
        Name: 
        Type: 
        Description: 
    """
    def get_playedTime(self):
        return dconverter.DurationConverter.get_time_str(self, vlc.libvlc_media_player_get_time(vlc_player))

    """
        Name: get_playedTime_ms
        Type: Method
        Description: Returns as milliseconds the current time 
        from VLC Media Player
    """
    def get_playedTime_ms(self):
        return vlc.libvlc_media_player_get_time(vlc_player)

    def get_songDuration_ms(self):
        return vlc.libvlc_media_player_get_length(vlc_player)

    def PlaySelectedPlaylist(self, playlist_urls):
        for song_url in playlist_urls:
            self.Play(self.prepare_media(self, song_url))
