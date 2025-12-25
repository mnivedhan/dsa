from typing import List

from lld_practice.spotify.playable import Playable
from lld_practice.spotify.song import Song


class Album(Playable):

    def __init__(self, _id, name):
        super().__init__(name)
        self.id = _id
        self.songs: List[Song] = []

    def get_tracks(self):
        return self.songs
