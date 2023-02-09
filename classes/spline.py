import pygame
import numpy as np

class Spline:
    def __init__(self, points, color=(0, 255, 0)):
        self.points = points
        self.color = color
        self.t = np.linspace(0, 1, num=100)
        self.positions = self.evaluate_spline(self.t)

    def evaluate_spline(self, t):
        positions = []
        for i in range(len(self.points) - 1):
            p0 = self.points[i]
            p1 = self.points[i + 1]
            m0 = np.array([p0.x, p0.y])
            m1 = np.array([p1.x, p1.y])
            positions.append(self.evaluate_segment(p0, p1, m0, m1, t))
        return np.concatenate(positions)

    def evaluate_segment(self, p0, p1, m0, m1, t):
        t2 = t * t
        t3 = t2 * t
        h00 = 2 * t3 - 3 * t2 + 1
        h10 = t3 - 2 * t2 + t
        h01 = -2 * t3 + 3 * t2
        h11 = t3 - t2
        return h00[:, np.newaxis] * m0 + h10[:, np.newaxis] * (p1.x - p0.x) + h01[:, np.newaxis] * m1 + h11[:, np.newaxis] * (p0.x - p1.x)

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, False, self.positions, 5)
