from pygame import Rect, Surface, draw
from dataclasses import dataclass

@dataclass
class Node:
    x: int
    y: int
    color: tuple[int, int, int] = (200, 50, 50)
    radius: int = 6

    hover_color = (212, 92, 42)
    is_hover = False

    def __post_init__(self):
        self.size = round(self.radius * 2.7)  # 2.7 is size multiplier
        self.rect = Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

    def get(self) -> tuple[int, int]:
        return self.x, self.y

    def draw(self, win: Surface) -> None:
        draw.circle(win, self.hover_color if self.is_hover else self.color, (int(self.x), int(self.y)), self.radius)

    def hover(self, pos):
        self.is_hover = self.rect.collidepoint(pos)
