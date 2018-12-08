import time
import xml.etree.cElementTree as xml_engine

playlist_name = None
playlist_songs = None

class PlaylistCreator:

    def __init__(self):
        global XMLroot
        XMLroot = xml_engine.Element("pls")

    def namePlaylist(self, name):
        xml_engine.SubElement(XMLroot, "pls_name").text = name
        return True

    def add_song_to_playlist(self, url):
        xml_engine.SubElement(XMLroot, "pls_song").text = url

    def save_playlist(self):
        data = xml_engine.ElementTree(XMLroot)
        filename = time.strftime("%d.%m.%y-%H.%M.%S")
        extension = ".glst"
        data.write(filename+extension)