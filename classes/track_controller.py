from random import randint

from classes.node import Node
from classes.track import Track

class TrackController:
    blueprint_color = (120, 120, 255)
    tracks = []

    def __init__(self):
        self.on = False
        self.color = (255, 100, 10)
        self.first_node = None
        self.second_node = None
        self.first_select = True

    def draw(self, win):
        for track in self.tracks:
            track.draw(win)

        if not (self.first_node is None):
            self.first_node.draw(win)
        if not (self.second_node is None):
            self.second_node.draw(win)

    def create_track(self):
        if self.first_node is not None and self.second_node is not None:
            self.first_node.color = (200, 50, 50)
            self.second_node.color = (200, 50, 50)

            new_track = Track((randint(20, 255), randint(20, 255), randint(20, 255)), self.first_node, self.second_node)
            self.tracks.append(new_track)

            for track in self.get_tracks_in_position(new_track.start_node.get(), new_track.end_node.get()):
                self.connect_tracks(track, new_track)

        self.first_node = None
        self.second_node = None

    def add_node(self, pos):
        pos = self.snap_pos_to_node(pos)

        if self.first_select:
            self.first_node = Node(pos[0], pos[1], color=self.blueprint_color)
        else:
            self.second_node = Node(pos[0], pos[1], color=self.blueprint_color)

        self.first_select = not self.first_select

    def snap_pos_to_node(self, pos):
        if (node := self.get_first_node_in_position(pos)) is not None:
            return node.get()

        return pos

    def get_first_node_in_position(self, pos):
        for track in self.tracks:
            if track.start_node.rect.collidepoint(pos):
                return track.start_node
            if track.end_node.rect.collidepoint(pos):
                return track.end_node

        return None

    def get_nodes_in_position(self, pos):
        nodes = []
        for track in self.tracks:
            if track.start_node.rect.collidepoint(pos):
                nodes.append(track.start_node)
            elif track.end_node.rect.collidepoint(pos):
                nodes.append(track.end_node)

        return nodes

    def get_tracks_in_position(self, *positions):
        return [track for track in self.tracks if len([pos for pos in positions if track.start_node.rect.collidepoint(pos) or track.end_node.rect.collidepoint(pos)])]

    def connect_tracks(self, track_one: Track, track_two: Track):
        track_one.connect_track(track_two)
        track_two.connect_track(track_one)
