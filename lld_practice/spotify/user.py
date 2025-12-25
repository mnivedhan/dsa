from typing import List

from lld_practice.spotify.artist import Artist
from lld_practice.spotify.observer import Observer
from lld_practice.spotify.playable import Playable
from lld_practice.spotify.song import Song


class User(Observer):

    def __init__(self, id, name, email):
        self._id = id
        self.name = name
        self.email = email
        self.followed_artist: List[Artist] = []

    def follow_artist(self, artist: Artist):
        self.followed_artist.append(artist)

    def on_update(self, artist: Artist, playable: Playable):
        print(f"Artist {artist} has added a playable {playable.name}")

    @property
    def id(self) -> str:
        return self._id
