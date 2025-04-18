from circleshape import *

class Asteroid(CircleShape):
    def __init_(self, x, y, radius):
        super().__init__(self, x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (x, y), 2)

    def update(self, dt):
        self.velocity += (self.velocity * dt)