from typing import List

from lld_practice.spotify.artist import Artist
from lld_practice.spotify.observer import Observer
from lld_practice.spotify.playable import Playable
from lld_practice.spotify.song import Song


class Subject:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observers(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, artist: Artist, playable: Playable):
        for observer in self.observers:
            observer.on_update(artist, playable)