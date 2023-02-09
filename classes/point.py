import pygame

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.size = 8
        self.radius = 8
        self.rect = pygame.Rect(x - self.size // 2, y - self.size // 2, self.size, self.size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def get(self):
        return self.x, self.y
