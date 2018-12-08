songIndex = None


class SongManager:

    def __init__(self):
        # Parse Selected Playlist
        global songIndex
        songIndex = 0

    def get_firstSong(self):
        print("d")

    def get_song(self,index):
        print("asf")

    def next_song(self):
        songIndex +=1
    def previous_song(self):
        songIndex -=1