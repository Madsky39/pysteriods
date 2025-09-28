import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split (self):
        new_radius = self.radius
        new_velocity = self.velocity.copy()
        position = self.position.copy()
        self.kill()
        if new_radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius -= ASTEROID_MIN_RADIUS
        random_angle= random.uniform(20,50)
        asteroid_one = Asteroid(position.x, position.y, new_radius)
        asteroid_two = Asteroid(position.x, position.y, new_radius)
        asteroid_one.velocity = new_velocity.rotate(random_angle)* 1.2 
        asteroid_two.velocity = new_velocity.rotate(-random_angle)* 1.2
