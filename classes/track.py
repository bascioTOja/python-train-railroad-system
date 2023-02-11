import pygame
from random import choice

class Track:
    def __init__(self, color, start_node, end_node):
        self.color = color
        self.start_node = start_node
        self.end_node = end_node
        self.connected_with_end = []
        self.connected_with_start = []
        self.block = False

    def draw(self, win):
        pygame.draw.line(win, self.color, self.start_node.get(), self.end_node.get(), 2)
        self.start_node.draw(win)
        self.end_node.draw(win)

    def get_new_target_node(self, current_target):
        if current_target.get() == self.start_node.get():
            return self.end_node
        else:
            return self.start_node

    def get_next_track(self, current_node):
        if current_node is self.start_node:
            if tracks := [track for track in self.connected_with_start if not track.block]:
                return choice(tracks)
        else:
            if tracks := [track for track in self.connected_with_end if not track.block]:
                return choice(tracks)

        return None

    def connect_track(self, track):
        # todo fix connect tracks
        if self.start_node.get() == track.start_node.get():
            self.connect_with_start(track)

        if self.start_node.get() == track.end_node.get():
            self.connect_with_start(track)

        if self.end_node.get() == track.start_node.get():
            self.connect_with_end(track)

        if self.end_node.get() == track.end_node.get():
            self.connect_with_end(track)

    def connect_with_start(self, track):
        self.connected_with_start.append(track)

    def connect_with_end(self, track):
        self.connected_with_end.append(track)
