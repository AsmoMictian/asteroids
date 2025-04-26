from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0   #next lines create properties on the Player object
        self.add(*self.__class__.containers)
        self.cool_timer = 0
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), [(int(p.x), int(p.y)) for p in self.triangle()], width=2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)                        
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE] and self.cool_timer <= 0: #inc cool down logic
            self.shoot()
            self.cool_timer = PLAYER_SHOOT_COOLDOWN
        self.cool_timer -= dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        bullet = Shot(int(self.position.x), int(self.position.y),SHOT_RADIUS) #instantiates a bullet
        forward = pygame.Vector2(0,1).rotate(self.rotation) #sets the velocity and rotational position
        bullet.velocity = forward * PLAYER_SHOOT_SPEED