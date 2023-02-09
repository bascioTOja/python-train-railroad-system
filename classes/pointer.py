from classes.point import Point

class Pointer:
    def __init__(self):
        self.coords = (0, 0)
        self.hold = False

    def pick_coord(self, pos):
        self.coords = pos

    def get_point(self):
        return Point(self.coords[0], self.coords[1])
