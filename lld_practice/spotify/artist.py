from typing import List

from lld_practice.spotify.album import Album
from lld_practice.spotify.subject import Subject


class Artist(Subject):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.albums_list: List[Album] = []

    def release_album(self, album: Album):
        self.albums_list.append(album)
        self.notify_observers(self, album)