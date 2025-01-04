# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {720}')
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(window, (0, 0, 0))

        pygame.display.flip()
        

if __name__ == "__main__":
    main()
