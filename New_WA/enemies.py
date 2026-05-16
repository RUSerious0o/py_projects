import pygame

from pygame.sprite import Sprite
from pygame.font import Font


class Enemy(Sprite):
    __DEFAULT_HP: int = 100
    __DEFAULT_DAMAGE = 1
    __DEFAULT_EXP_WIZARD: int = 1
    __DEFAULT_SIZE_IMAGE_BATTLE = (300, 300)

    main_image_path = ''
    hp = 1
    damage = 1
    exp_wizard = 1
    movement_speed = 45
    size_image_battle = (300, 300)

    def __init__(self, hp: int = __DEFAULT_HP, damage: int = __DEFAULT_DAMAGE, exp_wizard: int = __DEFAULT_EXP_WIZARD, size_image_battle: tuple = __DEFAULT_SIZE_IMAGE_BATTLE):
        super().__init__()
        self.dest = (0, 0)

        self.size_image_battle = size_image_battle if size_image_battle != Enemy.__DEFAULT_SIZE_IMAGE_BATTLE else self.size_image_battle

        self.image_world = pygame.transform.scale(pygame.image.load(self.main_image_path), (100, 66))
        self.image_battle = pygame.transform.scale(pygame.image.load(self.main_image_path), self.size_image_battle)
        self.image = self.image_world
        self.rect = self.image.get_rect()
        self.hp = hp if hp != Enemy.__DEFAULT_HP else self.hp / 10
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
    size_image_battle = (300, 300)


class Spider(Enemy):
    main_image_path = './images/spider.png'
    hp = 180
    damage = 40
    exp_wizard = 2
    size_image_battle = (300, 250)


class Mantis(Enemy):
    main_image_path = './images/man.png'
    hp = 330
    damage = 20
    exp_wizard = 2
    size_image_battle = (300, 250)


class Wasp(Enemy):
    main_image_path = './images/wasp_AI.png'
    hp = 90
    damage = 60
    exp_wizard = 2
    size_image_battle = (300, 250)


class Cockroach(Enemy):
    main_image_path = './images/cockroach_AI.png'
    hp = 260
    damage = 40
    exp_wizard = 3
    size_image_battle = (300, 300)


class Turtle(Enemy):
    main_image_path = './images/turtle_AI.png'
    hp = 600
    damage = 5
    exp_wizard = 1
    size_image_battle = (300, 250)


class Elephant(Enemy):
    main_image_path = './images/elephant.png'
    hp = 500
    damage = 50
    exp_wizard = 5
    size_image_battle = (300, 200)


class Thunder(Enemy):
    main_image_path = './images/thunder_AI.png'
    hp = 60
    damage = 200
    exp_wizard = 3
    size_image_battle = (300, 400)


class Dog(Enemy):
    main_image_path = './images/dog_AI.png'
    hp = 80
    damage = 70
    exp_wizard = 4
    size_image_battle = (300, 300)


class Cat(Enemy):
    main_image_path = './images/cat_AI.png'
    hp = 5000
    damage = 3
    exp_wizard = 5
    size_image_battle = (300, 250)
