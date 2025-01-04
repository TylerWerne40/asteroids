# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {720}')
    Clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updateable, drawable, shots)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    AF = AsteroidField()
    p = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(window, (0, 0, 0))
        dt = Clock.tick(60)/1000
        for i in updateable:
            i.update(dt)
        for i in drawable:
            i.draw(window)
        for i in asteroids:
            collide = i.collide_check(p)
            if collide:
                print("Game over!")
                sys.exit()
            for j in shots:
                if i.collide_check(j):
                    i.split()
                    j.kill()

        pygame.display.flip()

if __name__ == "__main__":
    main()
