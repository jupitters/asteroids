import pygame as pg
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
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

        if pg.key.get_pressed()[pg.K_SPACE]:
            shot = player.shoot()
            if shot:
                shots.add(shot)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                running = False
                break
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

        pg.display.flip()

        pg.display.set_caption(f"{clock.get_fps(): .1f}")
    

if __name__ == "__main__":
    main()