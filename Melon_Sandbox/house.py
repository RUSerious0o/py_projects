import pygame


class House(pygame.sprite.Sprite):
    def __init__(self, x, y, len_bricks, fundament, color, height_window, width_window, floors):
        super().__init__()
        self.len_bricks = len_bricks
        self.fundament = fundament
        self.color = color
        self.height_window = height_window
        self.width_window = width_window
        self.floors = floors
        self.image = pygame.Surface((20 * self.len_bricks, (20 * self.fundament + 20 * self.height_window) * 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
