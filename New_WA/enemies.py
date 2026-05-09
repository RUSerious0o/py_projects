import pygame

from pygame.sprite import Sprite
from pygame.font import Font


class Enemy(Sprite):
    main_image_path = ''

    def __init__(self):
        super().__init__()
        self.dest = (0, 0)
        self.image = pygame.image.load(self.main_image_path)
        self.rect = self.image.get_rect()
        self.hp = 0


class Bear(Enemy):
    main_image_path = './images/bear.png'

    def __init__(self, hp: int = 10):
        super().__init__()
        self.hp = hp


class Spider(Enemy):
    main_image_path = './images/spider.png'

    def __init__(self, hp: int = 13):
        super().__init__()
        self.hp = hp
