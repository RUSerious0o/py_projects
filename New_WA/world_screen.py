import random

import pygame
import sys
from pygame.sprite import Sprite

from ball import *
from enemies import *
from encounter_area import EncounterArea


class WorldScreen(Sprite):
    is_battle_scene = False

    def __init__(self, screen: pygame.Surface, sprites: list = [], bg_color: tuple = (6, 185, 30)):
        super().__init__()
        self.screen = screen
        self.bg_color = bg_color
        self.sprites = sprites

        self.current_enemy: Enemy = None
        self.encounter_areas = []
        self.player = None
        self.ball = None
        self.is_player_turn = True
        self.font_color = (255, 255, 98)
        self.font = pygame.font.Font(None, 36)
        self.enemy_battle_screen_position = (self.screen.get_width() / 4 * 3 - 150,
                                             self.screen.get_height() / 2 - 100)
        self.player_battle_screen_position = (self.screen.get_width() / 4 - 200,
                                              self.screen.get_height() / 2 - 200)
        self.player_world_screen_position = None
        self.world_map_image = pygame.image.load('./images/map.png')

        self.player_previous_position = (0, 0)

        self.preset_encounter_areas()

    def preset_encounter_areas(self):
        self.encounter_areas.append(EncounterArea(0, 0, 400, 400, [Bear, Spider, Wasp]))
        self.encounter_areas.append(EncounterArea(0, 450, 750, 350, [Mantis, Thunder, Turtle]))
        self.encounter_areas.append(EncounterArea(800, 500, 400, 300, [Cat, Elephant]))
        self.encounter_areas.append(EncounterArea(800, 0, 400, 450, [Cockroach, Dog]))

    def update(self):
        if not WorldScreen.is_battle_scene:
            self.draw_world_scene()
        else:
            self.draw_battle_scene()
            if self.is_player_turn:
                if self.ball:
                    return

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ball = PurpleBall()
                            self.ball.rect.x = self.screen.get_width() * 0.3
                            self.ball.rect.y = self.screen.get_height() * 0.5
                        if event.key == pygame.K_z:
                            self.ball = RedBall()
                            self.ball.rect.x = self.screen.get_width() * 0.2
                            self.ball.rect.y = self.screen.get_height() * 0.5
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            else:
                self.current_enemy.update()

                if self.current_enemy.rect.colliderect(self.player.rect):
                    self.player.hp -= self.current_enemy.damage
                    self.current_enemy.rect.x += self.current_enemy.movement_speed
                    self.current_enemy.is_attacking = False
                    self.current_enemy.is_returning = True

                if self.current_enemy.rect.x >= self.enemy_battle_screen_position[0]:
                    self.current_enemy.rect.x = self.enemy_battle_screen_position[0]
                    self.current_enemy.is_returning = False
                    self.is_player_turn = True

    def add_player(self, player: Sprite):
        self.player = player

    def add_sprite(self, sprite: Sprite, dest: tuple = (0, 0), m_scale: tuple = (200, 400)):
        sprite.image = pygame.transform.scale(sprite.image, m_scale)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = dest[0]
        sprite.rect.y = dest[1]

        self.sprites.append(sprite)

    def draw_world_scene(self):
        for encounter_area in self.encounter_areas:
            if encounter_area.collidepoint(self.player.rect.x, self.player.rect.y):
                player_position = self.player.rect.x, self.player.rect.y
                if player_position != self.player_previous_position:
                    self.player_previous_position = player_position
                    if random.randint(0, 100) > encounter_area.percent:
                        self.init_battle_scene(encounter_area.generate_enemy())
                        break

        self.screen.blit(self.world_map_image, (0, 0))

        for sprite in self.sprites:
            sprite.update()
            self.screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))

        if len(self.sprites) > 0:
            for sprite in self.sprites[1:]:
                if self.player.rect.colliderect(sprite.rect):
                    self.init_battle_scene(sprite)

        pygame.display.flip()

    def draw_battle_scene(self):
        player = self.player
        bg_color = (255, 125, 0)
        player_dest = self.player_battle_screen_position
        player.rect.x, player.rect.y = self.player_battle_screen_position
        enemy_dest = self.current_enemy.rect.x, self.current_enemy.rect.y

        self.screen.fill(bg_color)

        self.screen.blit(player.image, player_dest)
        self.screen.blit(self.current_enemy.image, enemy_dest)
        self.current_enemy.rect.x, self.current_enemy.rect.y = enemy_dest
        self.blit_battle_txt()

        if self.ball:
            self.screen.blit(self.ball.image, (self.ball.rect.x, self.ball.rect.y))
            self.ball.rect.x += self.ball.speed
            if self.ball.rect.colliderect(self.current_enemy.rect):
                self.current_enemy.hp -= self.ball.damage
                if isinstance(self.ball, RedBall):
                    PurpleBall.reset_mult()
                self.ball = None
                self.is_player_turn = False
                self.current_enemy.is_attacking = True

        pygame.display.flip()

        if self.current_enemy.hp <= 0:
            self.finish_battle()

        elif self.player.hp <= 0:
            pygame.quit()
            sys.exit()
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
        self.screen.blit(
            self.font.render(f'Текущий множитель = {PurpleBall.damage_mult}', True, self.font_color),
                 (self.screen.get_width() / 20, self.screen.get_height() / 20 + 50)
        )

    def init_battle_scene(self, sprite: Sprite):
        self.current_enemy = sprite
        self.current_enemy.image = self.current_enemy.image_battle
        self.current_enemy.rect = self.current_enemy.image.get_rect()
        self.current_enemy.rect.x, self.current_enemy.rect.y = self.enemy_battle_screen_position

        self.player_world_screen_position = (self.player.rect.x, self.player.rect.y)
        self.player.image = self.player.image_battle
        self.player.rect = self.player.image.get_rect()

        WorldScreen.is_battle_scene = True

    def finish_battle(self):
        WorldScreen.is_battle_scene = False

        # self.sprites.remove(self.current_enemy)
        Wizard.to_level -= self.current_enemy.exp_wizard
        self.current_enemy = None
        self.is_player_turn = True

        PurpleBall.reset_mult()

        if Wizard.to_level <= 0:
            Wizard.level += 1
            Wizard.to_level = 5 * Wizard.level
            self.player.hp *= 2
        self.player.image = self.player.image_world
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x, self.player.rect.y = self.player_world_screen_position
