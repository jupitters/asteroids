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
    
    def draw(selc, screen):
        pass
    def update(self, dt):
        pass