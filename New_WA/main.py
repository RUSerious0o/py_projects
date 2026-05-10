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
    world_screen.add_sprite(wizard, dest=(0, 0), m_scale=(100, 133))
    world_screen.add_sprite(bear, dest=(300, 300), m_scale=(100, 66))
    world_screen.add_sprite(Spider(), dest=(600, 300), m_scale=(100, 66))
    world_screen.add_sprite(Mantis(), dest=(900, 300), m_scale=(100, 66))
    world_screen.add_sprite(Wasp(), dest=(600, 500), m_scale=(100, 66))
    world_screen.add_sprite(Cockroach(), dest=(600, 100), m_scale=(100, 66))
    world_screen.add_sprite(Bear(), dest=(700, 100), m_scale=(100, 66))
    world_screen.add_sprite(Wasp(), dest=(523, 654), m_scale=(100, 66))
    world_screen.add_sprite(Bear(), dest=(657, 657), m_scale=(100, 66))
    world_screen.add_sprite(Cockroach(), dest=(132, 500), m_scale=(100, 66))
    world_screen.add_sprite(Turtle(), dest=(300, 500), m_scale=(100, 66))
    world_screen.add_sprite(Mantis(), dest=(700, 500), m_scale=(100, 66))
    world_screen.add_sprite(Elephant(), dest=(1000, 700), m_scale=(100, 66))
    world_screen.add_sprite(Elephant(), dest=(200, 100), m_scale=(100, 66))
    world_screen.add_sprite(Thunder(), dest=(300, 200), m_scale=(100, 66))
    world_screen.add_sprite(Thunder(), dest=(200, 600), m_scale=(100, 66))
    world_screen.add_sprite(Dog(), dest=(400, 600), m_scale=(100, 66))
    world_screen.add_sprite(Dog(), dest=(500, 300), m_scale=(100, 66))
    world_screen.add_sprite(Cat(), dest=(1100, 300), m_scale=(100, 66))
    world_screen.add_sprite(Cat(), dest=(450, 500), m_scale=(100, 66))

    run = True
    while run:
        clock.tick(fps)

        world_screen.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()
