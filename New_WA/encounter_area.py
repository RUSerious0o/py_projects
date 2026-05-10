import pygame
from random import randint


class EncounterArea(pygame.Rect):
    def __init__(self, x: float, y: float, width: float, height: float, enemies: list = [], percent: int = 99):
        super().__init__(x, y, width, height)
        self.enemies = enemies
        self.percent = percent

    def generate_enemy(self):
        return self.enemies[randint(0, len(self.enemies) - 1)]()
