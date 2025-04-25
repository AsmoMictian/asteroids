import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
    # Left edge (y values change, x is constant)
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(0, y * SCREEN_HEIGHT),
        ],
        # Right edge (y values change, x is constant)
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(SCREEN_WIDTH, y * SCREEN_HEIGHT),
        ],
        # Top edge (x values change, y is constant)
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, 0),
        ],
        # Bottom edge (x values change, y is constant)
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT),
        ],
]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            try:
                direction = edge[0].normalize()
            except ValueError:
                direction = pygame.Vector2(1, 0)  # default direction if normalization fails direction = edge[0].normalize()
            velocity = direction * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)