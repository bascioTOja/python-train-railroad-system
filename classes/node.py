from pygame import Rect, Surface, draw
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    track = None
    color: tuple[int, int, int] = (200, 50, 50)
    radius: int = 6

    hover_color = (212, 92, 42)
    is_hover = False

    def __post_init__(self):
        self.size = round(self.radius * 2.7)  # 2.7 is size multiplier
        self.rect = self.calculate_rect()

    def get(self) -> tuple[int, int]:
        return self.x, self.y

    def draw(self, win: Surface) -> None:
        draw.circle(win, self.hover_color if self.is_hover else self.color, (int(self.x), int(self.y)), self.radius)

    def hover(self, pos) -> None:
        self.is_hover = self.rect.collidepoint(pos)

    def move(self, pos) -> None:
        self.x, self.y = pos
        self.rect = self.calculate_rect()

    def calculate_rect(self) -> Rect:
        return Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

    def set_track(self, track: 'Track') -> None:
        self.track = track

    def is_in_pos(self, pos) -> bool:
        return self.rect.collidepoint(pos)

    def set_block(self, block: bool = True):
        self.track.set_block(block)
