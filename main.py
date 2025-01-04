# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {720}')
    Clock = pygame.time.Clock()
    dt = 0
    p = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(window, (0, 0, 0))

        p.draw(window)
        pygame.display.flip()
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
