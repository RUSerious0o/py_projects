import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard.png'

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Wizard.main_image_path)
