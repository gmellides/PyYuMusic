import pafy as networkMedia_worker


class MediaControl:

    def prepare_media(self, url):
        youtube_video = networkMedia_worker.new(url)
        audio = youtube_video.getbestaudio()
        return audio.url