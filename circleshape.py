import pygame as pg

class CircleShape(pg.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, 0)
        self.radius = radius
    
    def collision(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance <= (self.radius + CircleShape.radius)
    
    def draw(self, screen):
        pass
    def update(self, dt):
        pass
    