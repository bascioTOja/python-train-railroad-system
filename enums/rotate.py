from enum import Enum

class Rotate(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

    def get_next(self):
        return Rotate(self.value + 1 if self.value < 4 else 1)
