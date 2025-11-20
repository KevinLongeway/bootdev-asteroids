import random
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown_timer = max(0, self.shot_cooldown_timer - dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # Original:
    # def shoot(self):
        # if  self.shot_cooldown_timer > 0:
            # return
        # else:
            # shot = Shot(self.position.x, self.position.y)
            # shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            # self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    # Random shot direction and speed
    # def shoot(self):
        # if self.shot_cooldown_timer > 0:
            # return

        # Base direction the player is facing
        # direction = pygame.Vector2(0, 1).rotate(self.rotation)

        # 1. Add a small random spread (e.g. ±5 degrees)
        # spread = random.uniform(-5, 5)
        # direction = direction.rotate(spread)

        # 2. Randomize speed a bit around PLAYER_SHOT_SPEED
        # speed = random.uniform(0.9 * PLAYER_SHOT_SPEED, 1.1 * PLAYER_SHOT_SPEED)

        # shot = Shot(self.position.x, self.position.y)
        # shot.velocity = direction * speed

        # self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    # shotgun approach
    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return

        # Center direction (where the player is facing)
        base_direction = pygame.Vector2(0, 1).rotate(self.rotation)

        # How many shots and how wide the arc (in degrees)
        num_shots = 3   # vary this for more shots
        total_spread = 20  # total angle covered by the arc (e.g. -10, 0, +10), experiment with dif values

        if num_shots == 1:
            angles = [0]
        else:
            step = total_spread / (num_shots - 1)
            # e.g. for 3 shots and 20° spread: [-10, 0, 10]
            angles = [(-total_spread / 2) + i * step for i in range(num_shots)]

        for angle in angles:
            direction = base_direction.rotate(angle)

            # Optional: slight per-shot speed variation
            speed = random.uniform(0.9 * PLAYER_SHOT_SPEED, 1.1 * PLAYER_SHOT_SPEED)

            shot = Shot(self.position.x, self.position.y)
            shot.velocity = direction * speed

        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
