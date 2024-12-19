import pygame as pg
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, (128,128,128), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2