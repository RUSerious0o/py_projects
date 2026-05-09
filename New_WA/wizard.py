import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard.png'
    move_speed = 10

    def __init__(self, hp: int = 100):
        super().__init__()
        self.image = pygame.image.load(Wizard.main_image_path)
        self.rect = self.image.get_rect()
        self.hp = hp

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += Wizard.move_speed
        if keys[pygame.K_a]:
            self.rect.x -= Wizard.move_speed
        if keys[pygame.K_s]:
            self.rect.y += Wizard.move_speed
        if keys[pygame.K_w]:
            self.rect.y -= Wizard.move_speed

