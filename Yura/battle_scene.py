import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.font import Font

class BattleScene(Sprite):
    def __init__(self, screen: Surface, font: Font, player: Sprite, enemy: Sprite, bg_color: tuple = (255, 125, 0)):
        super().__init__()
        self.player = player
        self.enemy = enemy
        self.bg_color = bg_color
        self.screen = screen
        self.font = font

    def update(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.font.render('BATTLE!', True, (200, 255, 255)), (self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.enemy.blit_hp(self.screen, self.font)
        self.player.blit_hp(self.screen, self.font)

        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.screen.blit(self.enemy.image, (self.enemy.rect.x, self.enemy.rect.y))

        pygame.display.flip()
