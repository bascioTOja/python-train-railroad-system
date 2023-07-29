from dataclasses import dataclass

from classes.game import Game
from enums.rotate import Rotate


@dataclass
class Menu:
    game: Game
    rotate = Rotate.N

    def next_rotate(self):
        self.rotate = self.rotate.get_next()
