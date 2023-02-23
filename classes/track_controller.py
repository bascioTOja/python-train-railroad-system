from pygame import Surface
from random import randint
from typing import List, Union, Tuple
from dataclasses import dataclass, field

from classes.node import Node
from classes.track import Track


def connect_tracks(track_one: Track, track_two: Track) -> None:
    track_one.connect_track(track_two)
    track_two.connect_track(track_one)


@dataclass
class TrackController:
    blueprint_color: Tuple[int, int, int] = (120, 120, 255)
    tracks: List[Track] = field(default_factory=list)
    on: bool = False
    color: Tuple[int, int, int] = (255, 100, 10)
    first_node: Union[Node, None] = None
    second_node: Union[Node, None] = None
    first_select: bool = True

    def draw(self, win: Surface) -> None:
        for track in self.tracks:
            track.draw(win)

        if self.first_node is not None:
            self.first_node.draw(win)

        if self.second_node is not None:
            self.second_node.draw(win)

    def hover(self, pos: tuple[int, int]) -> None:
        for track in self.tracks:
            track.hover(pos)

    def create_track(self) -> None:
        if self.first_node is not None and self.second_node is not None:
            self.first_node.color = (200, 50, 50)
            self.second_node.color = (200, 50, 50)

            new_track = Track((randint(40, 170), randint(40, 170), randint(40, 170)), self.first_node, self.second_node)
            self.tracks.append(new_track)

            for track in self.get_tracks_in_position(new_track.start_node.get(), new_track.end_node.get(), with_out_track=new_track):
                connect_tracks(track, new_track)

        self.first_node = None
        self.second_node = None

    def add_node(self, pos: Tuple[int, int]) -> None:
        pos = self.snap_pos_to_node(pos)

        if self.first_select:
            self.first_node = Node(pos[0], pos[1], color=self.blueprint_color)
        else:
            self.second_node = Node(pos[0], pos[1], color=self.blueprint_color)

        self.first_select = not self.first_select

    def remove_node(self, pos: Tuple[int, int]) -> None:
        pos = self.snap_pos_to_node(pos)
        to_delete = self.get_tracks_in_position(pos, include_blocked=False)

        for track in to_delete:
            track.delete()

        self.tracks = [track for track in self.tracks if track not in to_delete]

    def snap_pos_to_node(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        if (node := self.get_first_node_in_position(pos)) is not None:
            return node.get()

        return pos

    def get_first_node_in_position(self, pos: Tuple[int, int]) -> Node | None:
        for track in self.tracks:
            if track.start_node.rect.collidepoint(pos):
                return track.start_node
            if track.end_node.rect.collidepoint(pos):
                return track.end_node

        return None

    def get_nodes_in_position(self, pos: Tuple[int, int]) -> List[Node]:
        nodes = []
        for track in self.tracks:
            if track.start_node.rect.collidepoint(pos):
                nodes.append(track.start_node)
            elif track.end_node.rect.collidepoint(pos):
                nodes.append(track.end_node)

        return nodes

    def get_first_track_in_position(self, pos: Tuple[int, int]) -> Track | None:
        return next((track for track in self.tracks if track.start_node.rect.collidepoint(pos) or track.end_node.rect.collidepoint(pos)), None)

    def get_tracks_in_position(self, *positions: Tuple[int, int], with_out_track: Union[Track, None] = None, include_blocked: bool = True, get_index: bool = False) -> List[int | Track]:
        return [index if get_index else track for index, track in enumerate(self.tracks) if (track is not with_out_track) and (include_blocked or not track.block) and len([pos for pos in positions if track.start_node.rect.collidepoint(pos) or track.end_node.rect.collidepoint(pos)])]
