import pygame
import math
from dataclasses import dataclass

from classes.node import Node
from classes.track import Track
from classes.train_types import get_train_type_class
from enums.train_type import TrainType


@dataclass
class Train:
    type_name: TrainType
    position: tuple[int, int]
    track: Track
    target_node: Node | None = None
    color: tuple[int, int, int] = (125, 255, 170)
    not_running_color: tuple[int, int, int] = (255, 0, 0)
    hover_color: tuple[int, int, int] = (255, 121, 66)
    running: bool = False

    is_hover = False
    angle = 0
    rotation = 0

    def __post_init__(self):
        self.x, self.y = self.position
        self.type = get_train_type_class(self.type_name)
        self.width, self.height = self.type.image.get_size()
        self.target_node = self.target_node or self.track.end_node

        self.update_position(None)
        self.update_rotation()

    def update(self, game = None) -> None:
        self.check_end_track()
        self.track.block = True
        if self.running:
            self.update_position(game)
            self.update_rotation()
        else:
            self.set_next_track()

    def hover(self, pos):
        self.is_hover = self.rect.collidepoint(pos)

    def draw(self, win: pygame.Surface) -> None:
        color = self.color if self.running else self.not_running_color

        pygame.draw.circle(win, self.hover_color if self.is_hover else color, self.rect.center, self.width//2)
        win.blit(self.rotated_image, self.rect)

    def delete(self):
        self.track.block = False
        del self

    def update_position(self, game):
        self.angle = math.atan2(self.target_node.y - self.y, self.target_node.x - self.x)
        delta_time = game.fps if game is not None else 60
        self.x += math.cos(self.angle) / delta_time * self.type.speed
        self.y += math.sin(self.angle) / delta_time * self.type.speed

    def update_rotation(self):
        self.rotation = math.degrees(-self.angle) - 90
        self.rotated_image = pygame.transform.rotate(self.type.image, self.rotation)
        self.rect = self.rotated_image.get_rect(center=(self.x, self.y))

    def set_next_track(self) -> None:
        next_track = self.track.get_next_track(self.target_node)
        if next_track is None:
            return None

        next_node = next_track.get_new_target_node(self.target_node)
        if next_node is None:
            return None

        self.track.block = False
        self.track = next_track
        self.track.block = True
        self.target_node = next_node
        self.running = True

    def check_end_track(self) -> None:
        offset = self.type.speed/60/2 # 60 fps
        distance_to_target = math.hypot(self.target_node.x - self.x, self.target_node.y - self.y)
        self.running = distance_to_target > offset
