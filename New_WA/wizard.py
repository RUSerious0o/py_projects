import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard.png'
    move_speed = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Wizard.main_image_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.dest = (self.dest[0] + Wizard.move_speed, self.dest[1])
        if keys[pygame.K_a]:
            self.dest = (self.dest[0] - Wizard.move_speed, self.dest[1])
        if keys[pygame.K_s]:
            self.dest = (self.dest[0], self.dest[1] + Wizard.move_speed)
        if keys[pygame.K_w]:
            self.dest = (self.dest[0], self.dest[1] - Wizard.move_speed)

