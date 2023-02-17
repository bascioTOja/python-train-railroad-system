import pygame
import math

class Train:
    not_running_color = (255, 0, 0)

    def __init__(self, position, track, image):
        self.x = position[0]
        self.y = position[1]
        self.image = image
        self.speed = 75
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.color = (125, 255, 170)
        self.track = track
        self.target_node = track.end_node
        self.rotated_image = None
        self.rect = None
        self.running = True
        self.update()

    def update(self, game = None):
        self.check_end_track()
        self.track.block = True
        if self.running:
            angle = math.atan2(self.target_node.y - self.y, self.target_node.x - self.x)

            self.x, self.y = (self.x + math.cos(angle) / (game.fps if game is not None else 60) * self.speed,
                            self.y + math.sin(angle) / (game.fps if game is not None else 60) * self.speed)

            rotation = math.degrees(-angle)
            self.rotated_image = pygame.transform.rotate(self.image, rotation-90)
            self.rect = self.rotated_image.get_rect(center=(self.x, self.y))
        else:
            self.set_next_track()

    def draw(self, win):
        pygame.draw.circle(win, self.color if self.running else self.not_running_color, (self.rect.center[0], self.rect.center[1]), self.width//2)
        win.blit(self.rotated_image, self.rect)

    def set_next_track(self):
        next_track = self.track.get_next_track(self.target_node)
        if next_track is None:
            return None

        next_node = next_track.get_new_target_node(self.target_node)

        if next_node is None:
            return None

        self.track.block = False
        self.track = next_track
        self.track.block = True
        self.target_node = next_node
        self.running = True

    def check_end_track(self):
        offset = self.speed/60/2  # 60 fps
        if ((self.x - offset) <= self.target_node.x <= (self.x + offset)) and ((self.y - offset) <= self.target_node.y <= (self.y + offset)):
            self.running = False
        else:
            self.running = True
