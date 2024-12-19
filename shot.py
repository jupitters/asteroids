import pygame as pg
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    
    def draw(self, screen):
        pg.draw.circle(screen, (255,255,255), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt