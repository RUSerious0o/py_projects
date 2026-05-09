import pygame

from pygame.sprite import Sprite
from pygame.font import Font


class Enemy(Sprite):
    __DEFAULT_HP: int = 10
    __DEFAULT_DAMAGE = 1

    main_image_path = ''
    hp = 1
    damage = 1
    movement_speed = 45

    def __init__(self, hp: int = __DEFAULT_HP, damage: int = __DEFAULT_DAMAGE):
        super().__init__()
        self.dest = (0, 0)
        self.image = pygame.image.load(self.main_image_path)
        self.rect = self.image.get_rect()
        self.hp = hp if hp != Enemy.__DEFAULT_HP else self.hp
        self.damage = damage if damage != Enemy.__DEFAULT_DAMAGE else self.damage
        self.is_attacking = False
        self.is_returning = False

    def update(self):
        if self.is_attacking:
            self.rect.x -= self.movement_speed
        if self.is_returning:
            self.rect.x += self.movement_speed


class Bear(Enemy):
    main_image_path = './images/bear.png'
    hp = 12
    damage = 3


class Spider(Enemy):
    main_image_path = './images/spider.png'
    hp = 18
    damage = 4


class Mantis(Enemy):
    main_image_path = './images/mantis.png'
    hp = 33
    damage = 2


class Wasp(Enemy):
    main_image_path = './images/wasp.png'
    hp = 9
    damage = 6


class Cockroach(Enemy):
    main_image_path = './images/cockroach.png'
    hp = 26
    damage = 4

