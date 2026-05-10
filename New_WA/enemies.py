import pygame

from pygame.sprite import Sprite
from pygame.font import Font


class Enemy(Sprite):
    __DEFAULT_HP: int = 100
    __DEFAULT_DAMAGE = 1
    __DEFAULT_EXP_WIZARD: int = 1

    main_image_path = ''
    hp = 1
    damage = 1
    exp_wizard = 1
    movement_speed = 45

    def __init__(self, hp: int = __DEFAULT_HP, damage: int = __DEFAULT_DAMAGE, exp_wizard: int = __DEFAULT_EXP_WIZARD):
        super().__init__()
        self.dest = (0, 0)
        self.image_world = pygame.transform.scale(pygame.image.load(self.main_image_path), (100, 66))
        self.image_battle = pygame.transform.scale(pygame.image.load(self.main_image_path), (300, 200))
        self.image = self.image_world
        self.rect = self.image.get_rect()
        self.hp = hp if hp != Enemy.__DEFAULT_HP else self.hp
        self.damage = damage if damage != Enemy.__DEFAULT_DAMAGE else self.damage
        self.exp_wizard = exp_wizard if exp_wizard != Enemy.__DEFAULT_EXP_WIZARD else self.exp_wizard
        self.is_attacking = False
        self.is_returning = False

    def update(self):
        if self.is_attacking:
            self.rect.x -= self.movement_speed
        if self.is_returning:
            self.rect.x += self.movement_speed


class Bear(Enemy):
    main_image_path = './images/bear.png'
    hp = 120
    damage = 30
    exp_wizard = 1


class Spider(Enemy):
    main_image_path = './images/spider.png'
    hp = 180
    damage = 40
    exp_wizard = 2


class Mantis(Enemy):
    main_image_path = './images/mantis.png'
    hp = 330
    damage = 20
    exp_wizard = 2


class Wasp(Enemy):
    main_image_path = './images/wasp.png'
    hp = 90
    damage = 60
    exp_wizard = 2


class Cockroach(Enemy):
    main_image_path = './images/cockroach.png'
    hp = 260
    damage = 40
    exp_wizard = 3


class Turtle(Enemy):
    main_image_path = './images/turtle.png'
    hp = 600
    damage = 5
    exp_wizard = 1


class Elephant(Enemy):
    main_image_path = './images/elephant.png'
    hp = 500
    damage = 50
    exp_wizard = 5


class Thunder(Enemy):
    main_image_path = './images/thunder.png'
    hp = 60
    damage = 200
    exp_wizard = 3


class Dog(Enemy):
    main_image_path = './images/dog.png'
    hp = 80
    damage = 70
    exp_wizard = 4


class Cat(Enemy):
    main_image_path = './images/cat.png'
    hp = 5000
    damage = 3
    exp_wizard = 5
