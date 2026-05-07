import pygame

from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.dest = (0, 0)
        self.image = None


class Bear(Enemy):
    main_image_path = './images/bear.png'

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Bear.main_image_path)
        self.rect = self.image.get_rect()
