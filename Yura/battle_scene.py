import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface


class BattleScene(Sprite):
    def __init__(self, screen: Surface, player: Sprite, enemy: Sprite, bg_color: tuple = (255, 125, 0)):
        super().__init__()
        self.player = player
        self.enemy = enemy
        self.bg_color = bg_color
        self.screen = screen

    def update(self):
        self.screen.fill(self.bg_color)
