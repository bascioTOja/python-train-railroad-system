import pygame
from dataclasses import dataclass

@dataclass
class Node:
    x: int
    y: int
    color: tuple[int, int, int] = (200, 50, 50)
    radius: int = 6

    def __post_init__(self):
        self.size = round(self.radius * 2.7)  # 2.7 is size multiple
        self.rect = pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)

    def get(self) -> tuple[int, int]:
        return self.x, self.y
