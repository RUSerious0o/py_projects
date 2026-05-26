import pygame
import sys

from rendered import Rendered
from house import House

pygame.init()
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Горный Мегаполис - Melon Sandbox')

rendered = Rendered(screen)

houses_list = [
    House(150, 200, 11, 2, (200, 200, 200), 4, 4, 3),
    House(450, 320, 13, 2, (255, 255, 255), 4, 5, 3),
    House(800, 440, 15, 3, (150, 150, 150), 5, 6, 2)
]

clock = pygame.time.Clock()
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((135, 206, 235))
        rendered.draw_all_houses(houses_list)
        pygame.display.flip()
        clock.tick(60)
