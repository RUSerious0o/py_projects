import pygame
from pygame.sprite import Sprite


class WorldScreen(Sprite):
    def __init__(self, screen: pygame.Surface, sprites: list = [], bg_color: tuple = (6, 185, 30)):
        super().__init__()
        self.screen = screen
        self.bg_color = bg_color
        self.sprites = sprites

    def update(self):
        self.screen.fill(self.bg_color)

        for sprite in self.sprites:
            sprite.update()
            self.screen.blit(sprite.image, sprite.dest)

        pygame.display.flip()

    def add_sprite(self, sprite: Sprite, dest: tuple = (0, 0), m_scale: tuple = (200, 400)):
        sprite.dest = dest
        sprite.image = pygame.transform.scale(sprite.image, m_scale)
        self.sprites.append(sprite)
