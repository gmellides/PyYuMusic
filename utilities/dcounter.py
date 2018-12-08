

class DurationCounter:

    def get_time_str(self, ms):
        media_sec = ms / 1000
        # from 1 to 9 -> 09
        if int(media_sec) < 10:
            value = "{}{}:{}{}".format(0, 0, 0, int(media_sec))
        # from 10
        elif int(media_sec) >= 10 and int(media_sec) < 60:
            value = "{}{}:{}".format(0, 0, int(media_sec))
        elif int(media_sec) >= 60:
            minute = int(media_sec) / 60
            seconds = int(media_sec) % 60
            if seconds < 10:
                value = "{}{}:{}{}".format(0, int(minute), 0, seconds)
            elif seconds >= 10 and seconds < 60:
                value = "{}{}:{}".format(0, int(minute), seconds)
        return value