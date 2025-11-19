import pygame
import random
from  circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        # Original:
        angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(angle)
        direction2 = self.velocity.rotate(-angle)

        # Experiment: two independent random angles
        # angle1 = random.uniform(-50, 50)
        # angle2 = random.uniform(-50, 50)

        # direction1 = self.velocity.rotate(angle1)
        # direction2 = self.velocity.rotate(angle2)
        # new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Original:
        new_asteroid1.velocity = direction1 * 1.2
        new_asteroid2.velocity = direction2 * 1.2

        # different speeds for each split
        # speed1 = random.uniform(1.1, 1.4)
        # speed2 = random.uniform(1.1, 1.4)

        # new_asteroid1.velocity = direction1 * speed1
        # new_asteroid2.velocity = direction2 * speed2

        # smaller radius → faster asteroid
        # speed_factor = 1.0 + (ASTEROID_MIN_RADIUS / new_radius)   # hardest
        # speed_factor = 1.0 + 0.5 * (ASTEROID_MIN_RADIUS / new_radius)   # easier

        # new_asteroid1.velocity = direction1 * speed_factor
        # new_asteroid2.velocity = direction2 * speed_factor
