import pygame
import math

class Train:
    not_running_color = (255, 0, 0)

    def __init__(self, position, track):
        self.x = position[0]
        self.y = position[1]
        self.speed = 50
        self.width = 8
        self.height = 20
        self.color = (100, 100, 255)
        self.track = track
        self.target_node = track.end_node
        self.rect_points = []
        self.a = (0, 0)
        self.b = (0, 0)
        self.c = (0, 0)
        self.d = (0, 0)
        self.running = True
        self.update()

    def update(self, game = None):
        self.check_end_track()
        if self.running:
            angle = math.atan2(self.target_node.y - self.y, self.target_node.x - self.x)

            self.x, self.y = (self.x + math.cos(angle) / (game.fps if not game is None else 60) * self.speed,
                             self.y + math.sin(angle) / (game.fps if not game is None else 60) * self.speed)

            self.a = (self.x - math.sin(angle) * self.width / 2 + math.cos(angle) * self.height / 2, self.y - math.cos(angle) * self.width / 2 - math.sin(angle) * self.height / 2)
            self.b = (self.x + math.sin(angle) * self.width / 2 + math.cos(angle) * self.height / 2, self.y + math.cos(angle) * self.width / 2 - math.sin(angle) * self.height / 2)
            self.c = (self.x + math.sin(angle) * self.width / 2 - math.cos(angle) * self.height / 2, self.y + math.cos(angle) * self.width / 2 + math.sin(angle) * self.height / 2)
            self.d = (self.x - math.sin(angle) * self.width / 2 - math.cos(angle) * self.height / 2, self.y - math.cos(angle) * self.width / 2 + math.sin(angle) * self.height / 2)


            self.rect_points = [self.a, self.b, self.c, self.d]
        else:
            self.set_next_track()

    def set_next_track(self):
        next_track = self.track.get_next_track(self.target_node)
        if next_track is None:
            return None

        next_node = next_track.get_new_target_node(self.target_node)

        if next_node is None:
            return None

        self.track = next_track
        self.target_node = next_node
        self.running = True

    def draw(self, win):
        if len(self.rect_points) > 2:
            pygame.draw.polygon(win, self.color if self.running else self.not_running_color, self.rect_points)
            pygame.draw.circle(win, (0, 0, 255), self.a, 2)
            pygame.draw.circle(win, (0, 255, 0), self.b, 2)
            pygame.draw.circle(win, (255, 0, 0), self.c, 2)
            pygame.draw.circle(win, (255, 0, 255), self.d, 2)

    def check_end_track(self):
        offset = self.speed/60/2  # 60 fps
        if ((self.x - offset) <= self.target_node.x <= (self.x + offset)) and ((self.y - offset) <= self.target_node.y <= (self.y + offset)):
            self.running = False
