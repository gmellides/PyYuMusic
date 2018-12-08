import pafy


class SongInfo:

    def get_song_title(self, url):
        global youtube_video
        youtube_video = pafy.new(url)
        return youtube_video.title

    def get_song_duration(self):
        h, m, s = youtube_video.duration.split(":")
        if int(h) > 0:
            value = youtube_video.duration
        else:
            value = "{}:{}".format(m, s)
        return value
