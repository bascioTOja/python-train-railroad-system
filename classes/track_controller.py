from classes.point import Point
from classes.track import Track

class TrackController:
    def __init__(self):
        self.tracks = []
        self.blueprint_color = (120, 120, 255)
        self.color = (255, 100, 10)
        self.pre_track = Track(self.blueprint_color)

    def add_point(self, point: Point):
        self.pre_track.add_point(point)

        if len(self.pre_track.control_points) >= 4:
            self.pre_track.color = self.color
            self.tracks.append(self.pre_track)

            self.pre_track = Track(self.blueprint_color, [point])

    def add_track(self, track):
        self.tracks.append(track)

    def draw(self, win):
        self.pre_track.draw(win)
        for track in self.tracks:
            track.draw(win)
