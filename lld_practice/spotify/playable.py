from abc import ABC, abstractmethod
from tkinter.font import names


class Playable(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_tracks(self):
        pass
