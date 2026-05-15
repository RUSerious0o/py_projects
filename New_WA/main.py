import pygame
import sys

from world_screen import WorldScreen

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
fps = 60

world_screen = WorldScreen(screen)


if __name__ == '__main__':
    run = True
    while run:
        clock.tick(fps)

        world_screen.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()
