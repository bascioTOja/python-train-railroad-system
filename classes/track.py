import pygame

class Track:
    def __init__(self, color, start_node, end_node):
        self.color = color
        self.start_node = start_node
        self.end_node = end_node
        self.connected_with_end = []
        self.connected_with_start = []
        self.block = False

    def get_new_target_node(self, current_target):
        if current_target.get() == self.start_node.get():
            return self.end_node
        else:
            return self.start_node

    def get_next_track(self, current_node):
        if current_node is self.start_node:
            if not len(self.connected_with_start):
                return None
            else:
                for track in self.connected_with_start:
                    if not track.block:
                        return track
                return None
        else:
            if not len(self.connected_with_end):
                return None
            else:
                for track in self.connected_with_end:
                    if not track.block:
                        return track
        return None

    def draw(self, win):
        pygame.draw.line(win, self.color, self.start_node.get(), self.end_node.get(), 2)
