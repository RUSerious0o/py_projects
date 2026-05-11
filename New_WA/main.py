import pygame
import sys

from world_screen import WorldScreen
from encounter_area import EncounterArea
from wizard import Wizard
from enemies import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
fps = 60

wizard = Wizard()
world_screen = WorldScreen(screen)


if __name__ == '__main__':
    world_screen.add_player(wizard)
    world_screen.add_sprite(wizard, dest=(90, 90), m_scale=(50, 66))

    run = True
    while run:
        clock.tick(fps)

        world_screen.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()
