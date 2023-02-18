import pygame
from dataclasses import dataclass

@dataclass
class Game:
    size: tuple[int, int]
    fps: int
    run: bool = True

    def __post_init__(self):
        self.width = self.size[0]
        self.height = self.size[1]
        self.win = pygame.display.set_mode(self.get_size())
        self.clock = pygame.time.Clock()

    def draw(self, *args) -> None:
        self.win.fill((0, 0, 0))
        for item in args:
            item.draw(self.win)
        pygame.display.update()

    def update(self, *args) -> None:
        for item in args:
            item.update(self)

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height
