from dataclasses import dataclass

import pygame

from classes.game import Game
from classes.node import Node
from enums.rotate import Rotate
from enums.track_type import TrackType
from classes.track import Track

track_images = {
    TrackType.NORMAL: pygame.image.load("images\\normal_track.png"),
}

@dataclass
class TrackFactory(object):
    game: Game
    # Make this more self-service
    def create_track(self, track_type: TrackType, coords: (int, int), rotate: Rotate) -> Track:
        return Track(
            image=track_images[track_type],
            color=(200, 250, 10),
            coords=coords,
            rotate=rotate,
            start_node=self.get_start_node(coords, rotate),
            end_node=self.get_end_node(coords, rotate),
        )

    def get_start_node(self, coords: (int, int), rotate: Rotate) -> Node:
        full_offset = self.game.grid_size
        half_offset = full_offset // 2

        if rotate == rotate.N:
            return Node(coords[0] + half_offset, coords[1] )

        if rotate == rotate.E:
            return Node(coords[0] + full_offset, coords[1] + half_offset)

        if rotate == rotate.S:
            return Node(coords[0] + half_offset, coords[1] + full_offset)

        if rotate == rotate.W:
            return Node(coords[0], coords[1] + half_offset)

    def get_end_node(self, coords: (int, int), rotate: Rotate) -> Node:
        full_offset = self.game.grid_size
        half_offset = full_offset // 2

        if rotate == rotate.N:
            return Node(coords[0] + half_offset, coords[1] + full_offset)

        if rotate == rotate.E:
            return Node(coords[0], coords[1] + half_offset)

        if rotate == rotate.S:
            return Node(coords[0] + half_offset, coords[1] )

        if rotate == rotate.W:
            return Node(coords[0] + full_offset, coords[1] + half_offset)
