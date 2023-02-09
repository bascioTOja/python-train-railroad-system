import pygame


class Game:
    def __init__(self, size, fps):
        self.width = size[0]
        self.height = size[1]
        self.fps = fps

        self.win = pygame.display.set_mode(self.get_size())
        self.clock = pygame.time.Clock()
        self.run = True

    def draw(self, *args):
        self.win.fill((0, 0, 0))

        for item in args:
            item.draw(self.win)

        pygame.display.update()

    def update(self, *args):
        for item in args:
            item.update(self)

    def get_size(self):
        return self.width, self.height
