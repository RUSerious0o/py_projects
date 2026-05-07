import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard.png'

    def __init__(self):
        super().__init__()
        self.dest = (0, 0)
        self.image = pygame.image.load(Wizard.main_image_path)
        self.image = pygame.transform.scale(self.image, (200, 400))
