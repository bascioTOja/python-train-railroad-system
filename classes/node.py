import pygame

class Node:
    def __init__(self, x: int, y: int, color = (200, 50, 50)):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 6
        self.size = self.radius * 2.7
        self.rect = pygame.Rect(x - self.size // 2, y - self.size // 2, self.size, self.size)
        self.block = False

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def get(self) -> (int, int):
        return self.x, self.y
