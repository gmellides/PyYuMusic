import os
import xml.etree.cElementTree as xml_mechanism

song_urls = []


class PlaylistParser:

        def __init__(self, filename):
            global selected_list
            global song_urls
            selected_list = filename

        def get_song_list(self):
            pos = 0
            doc = xml_mechanism.ElementTree(file=selected_list)
            root = doc.getroot()
            for subelement in root:
                if subelement.tag == "pls_song":
                    song_urls.insert(pos, subelement.text)
                    pos+=1
            return song_urls