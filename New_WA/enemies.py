import pygame

from pygame.sprite import Sprite
from pygame.font import Font


class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.dest = (0, 0)
        self.image = None
        self.hp = 0


class Bear(Enemy):
    main_image_path = './images/bear.png'

    def __init__(self, hp: int = 10):
        super().__init__()
        self.image = pygame.image.load(Bear.main_image_path)
        self.rect = self.image.get_rect()
        self.hp = hp
