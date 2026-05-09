import pygame
import sys

from world_screen import WorldScreen
from wizard import Wizard
from enemies import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
fps = 60

world_screen = WorldScreen(screen)
wizard = Wizard()
bear = Bear()

if __name__ == '__main__':
    world_screen.add_player(wizard)
    world_screen.add_sprite(wizard)
    world_screen.add_sprite(bear, dest=(300, 300), m_scale=(300, 200))
    world_screen.add_sprite(Spider(), dest=(600, 300), m_scale=(300, 200))
    world_screen.add_sprite(Mantis(), dest=(900, 300), m_scale=(300, 200))
    world_screen.add_sprite(Wasp(), dest=(600, 500), m_scale=(300, 200))
    world_screen.add_sprite(Cockroach(), dest=(600, 100), m_scale=(300, 200))

    run = True
    while run:
        clock.tick(fps)

        world_screen.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()
