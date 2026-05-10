import pygame

from pygame.sprite import Sprite

from wizard import Wizard


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.damage = 10 * Wizard.level
        self.image = None
        self.speed = 30


class PurpleBall(Ball):
    image_path = './images/purple_ball.png'
    damage_mult = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PurpleBall.image_path)
        self.rect = self.image.get_rect()
        PurpleBall.damage_mult += 1

    @staticmethod
    def reset_mult():
        PurpleBall.damage_mult = 1


class RedBall(Ball):
    image_path = './images/red_ball.png'

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RedBall.image_path)
        self.rect = self.image.get_rect()
        self.damage = 20 * PurpleBall.damage_mult * Wizard.level
