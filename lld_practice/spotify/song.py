from lld_practice.spotify.playable import Playable


class Song(Playable):

    def __init__(self, _id, name, duration, artist):
        super().__init__(name)
        self.id = _id
        self.duration = duration,
        self.artist = artist

    def get_tracks(self):
        return [self]
