from pygame import Surface, draw
from random import choice
from typing import List, Union
from dataclasses import dataclass, field

from classes.node import Node
from enums.rotate import Rotate

@dataclass
class Track:
    color: tuple[int, int, int]
    start_node: Node
    end_node: Node
    coords: (int, int) = None
    rotate: Rotate = None
    image: Surface|None = None
    connected_with_end: List['Track'] = field(default_factory=list)
    connected_with_start: List['Track'] = field(default_factory=list)
    block: bool = False

    def __post_init__(self):
        self.start_node.set_track(self)
        self.end_node.set_track(self)

    def draw(self, win: Surface) -> None:
        if self.image and self.coords:
            win.blit(self.image, self.coords)

        draw.line(win, self.color, self.start_node.get(), self.end_node.get(), 2)
        self.start_node.draw(win)
        self.end_node.draw(win)

    def hover(self, pos: tuple[int, int]):
        self.start_node.hover(pos)
        self.end_node.hover(pos)

    def get_new_target_node(self, current_target: Node) -> Node:
        if current_target.get() == self.start_node.get():
            return self.end_node

        return self.start_node

    def get_next_track(self, current_node: Node) -> Union['Track', None]:
        if current_node is self.start_node:
            if tracks := [track for track in self.connected_with_start if not track.block]:
                return choice(tracks)
        elif tracks := [track for track in self.connected_with_end if not track.block]:
            return choice(tracks)

        return None

    def delete(self) -> None:
        for track in self.connected_with_start:
            track.disconnect_track(self)

        for track in self.connected_with_end:
            track.disconnect_track(self)

    def get_node_by_pos(self, pos) -> None | Node:
        if self.start_node.is_in_pos(pos):
            return  self.start_node

        return self.end_node if self.end_node.is_in_pos(pos) else None

    def get_connections_by_node(self, node: Node):
        if node is self.start_node:
            return self.connected_with_start

        return self.connected_with_end if node is self.end_node else []

    def connect_track(self, track: 'Track') -> None:
        if self is Track:
            return

        if track in self.connected_with_start or track in self.connected_with_end:
            return

        if self.start_node.get() == track.start_node.get():
            self.connect_with_start(track)

        if self.start_node.get() == track.end_node.get():
            self.connect_with_start(track)

        if self.end_node.get() == track.start_node.get():
            self.connect_with_end(track)

        if self.end_node.get() == track.end_node.get():
            self.connect_with_end(track)

    def disconnect_track(self, track: 'Track') -> None:
        self.connected_with_start = [connected_track for connected_track in self.connected_with_start if connected_track is not track]
        self.connected_with_end = [connected_track for connected_track in self.connected_with_end if connected_track is not track]

    def disconnect_self_by_node(self, node: Node) -> None:
        if node is self.start_node:
            self.disconnect_self_start()
        elif node is self.end_node:
            self.disconnect_self_end()

    def disconnect_self_start(self) -> None:
        for track in self.connected_with_start:
            track.disconnect_track(self)

        self.connected_with_start = []

    def disconnect_self_end(self) -> None:
        for track in self.connected_with_end:
            track.disconnect_track(self)

        self.connected_with_end = []

    def connect_with_start(self, track: 'Track') -> None:
        self.connected_with_start.append(track)

    def connect_with_end(self, track: 'Track') -> None:
        self.connected_with_end.append(track)

    def set_block(self, block: bool = True) -> None:
        self.block = block
