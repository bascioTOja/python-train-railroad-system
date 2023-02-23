import pygame
from dataclasses import dataclass

from classes import helpers
from classes.track_controller import TrackController
from classes.train_controller import TrainController

@dataclass
class Game:
    size: tuple[int, int]
    fps: int
    run: bool = True
    pos: tuple[int, int] = (0, 0)

    def __post_init__(self):
        self.width = self.size[0]
        self.height = self.size[1]
        self.win = pygame.display.set_mode(self.get_size())
        self.clock = pygame.time.Clock()

        self.track_controller = TrackController()


        tracks, trains = helpers.create_tracks_and_trains()
        self.track_controller.tracks.extend(tracks)
        self.train_controller = TrainController(trains)

    def draw(self, *args) -> None:
        self.win.fill((0, 0, 0))
        for item in args:
            item.draw(self.win)
        pygame.display.update()

    def update(self, *args) -> None:
        for item in args:
            item.update(self)

    def hover(self, *args) -> None:
        for item in args:
            item.hover(self.pos)

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height
