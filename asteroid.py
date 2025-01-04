import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            vec1 = self.velocity.rotate(angle)

            vec2 = self.velocity.rotate(-angle)
            A1 = Asteroid(self.position.x, self.position.y, new_r)
            A2 = Asteroid(self.position.x, self.position.y, new_r)
            A1.velocity = vec1*1.2
            A2.velocity = vec2*1.2
