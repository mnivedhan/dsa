from abc import ABC, abstractmethod

from lld_practice.spotify.artist import Artist
from lld_practice.spotify.song import Song
from low_level_design.solutions.musicstreamingservice.playable import Playable


class Observer(ABC):

    @abstractmethod
    def on_update(self, artist: Artist, playable: Playable):
        pass
