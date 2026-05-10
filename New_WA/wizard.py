import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard_AI_2.png'
    move_speed = 10
    level = 1
    to_level = 5


    def __init__(self, hp: int = 1000):
        super().__init__()
        self.image_world = pygame.transform.scale(pygame.image.load(Wizard.main_image_path), (100, 133))
        self.image_battle = pygame.transform.scale(pygame.image.load(Wizard.main_image_path), (300, 400))

        self.image = self.image_world
        self.rect = self.image.get_rect()
        self.hp = hp

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.x < 1130:
            self.rect.x += Wizard.move_speed
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= Wizard.move_speed
        if keys[pygame.K_s] and self.rect.y < 670:
            self.rect.y += Wizard.move_speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= Wizard.move_speed

