import pygame as pg
from constants import *
from player import *

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0,0,0))
        dt = clock.tick(FPS) / 1000

        for objects in updatable:
            objects.update(dt)
            
        for objects in drawable:
            objects.draw(screen)

        pg.display.flip()

        pg.display.set_caption(f"{clock.get_fps(): .1f}")
    

if __name__ == "__main__":
    main()