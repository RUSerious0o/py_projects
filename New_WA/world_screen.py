import pygame
from pygame.sprite import Sprite


class WorldScreen(Sprite):
    is_battle_scene = False

    def __init__(self, screen: pygame.Surface, sprites: list = [], bg_color: tuple = (6, 185, 30)):
        super().__init__()
        self.screen = screen
        self.bg_color = bg_color
        self.sprites = sprites

        self.current_enemy = None
        self.player = None
        self.font_color = (255, 255, 98)
        self.font = pygame.font.Font(None, 36)

    def update(self):
        if not WorldScreen.is_battle_scene:
            self.draw_world_scene()
        else:
            self.draw_battle_scene()

    def add_player(self, player: Sprite):
        self.player = player

    def add_sprite(self, sprite: Sprite, dest: tuple = (0, 0), m_scale: tuple = (200, 400)):
        sprite.image = pygame.transform.scale(sprite.image, m_scale)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = dest[0]
        sprite.rect.y = dest[1]

        self.sprites.append(sprite)

    def draw_world_scene(self):
        self.screen.fill(self.bg_color)

        for sprite in self.sprites:
            sprite.update()
            self.screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))

        if len(self.sprites) > 0:
            for sprite in self.sprites[1:]:
                if self.player.rect.colliderect(sprite.rect):
                    self.current_enemy = sprite
                    WorldScreen.is_battle_scene = True

        pygame.display.flip()

    def draw_battle_scene(self):
        player = self.player
        bg_color = (255, 125, 0)
        player_dest = (self.screen.get_width() / 4 - player.rect.width / 2,
                       self.screen.get_height() / 2 - player.rect.height / 2)
        enemy_dest = (self.screen.get_width() / 4 * 3 - self.current_enemy.rect.width / 2,
                      self.screen.get_height() / 2 - self.current_enemy.rect.height / 2)

        self.screen.fill(bg_color)

        self.screen.blit(player.image, player_dest)
        self.screen.blit(self.current_enemy.image, enemy_dest)
        self.blit_battle_txt()

        pygame.display.flip()

    def blit_battle_txt(self):
        self.screen.blit(
            self.font.render(f'Хп игрока = {self.player.hp}', True, self.font_color),
            (self.screen.get_width() / 20, self.screen.get_height() / 20)
        )
        self.screen.blit(
            self.font.render(f'Хп врага = {self.current_enemy.hp}', True, self.font_color),
            (self.screen.get_width() * 0.8, self.screen.get_height() / 20)
        )
        self.screen.blit(
            self.font.render('БИТВА!', True, self.font_color),
            (self.screen.get_width() * 0.5, self.screen.get_height() * 0.3)
        )
