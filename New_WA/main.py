import pygame

from world_screen import WorldScreen
from wizard import Wizard

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
fps = 60

world_screen = WorldScreen(screen)
wizard = Wizard()

if __name__ == '__main__':
    pygame.init()

    world_screen.add_sprite(wizard)

    run = True
    while run:
        clock.tick(fps)

        world_screen.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
