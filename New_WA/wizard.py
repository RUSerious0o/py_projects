import pygame
from pygame.sprite import Sprite


class Wizard(Sprite):
    main_image_path = './images/wizard_AI_2.png'
    secondary_image_path = './images/wizard_!!!.png'
    move_speed = 10
    level = 1
    to_level = 5
    world_map_image_size = (50, 66)
    world_map_in_encounter_area_image_size = (16, 22)
    battle_scene_size = (300, 400)

    def __init__(self, hp: int = 1000):
        super().__init__()
        self.image_world = pygame.transform.scale(pygame.image.load(Wizard.main_image_path), self.world_map_image_size)
        self.image_battle = pygame.transform.scale(pygame.image.load(Wizard.main_image_path), self.battle_scene_size)

        self.image = self.image_world
        self.image_in_encounter_area = pygame.image.load(self.secondary_image_path)
        self.image_in_encounter_area = pygame.transform.scale(self.image_in_encounter_area, self.world_map_in_encounter_area_image_size)
        self.rect = self.image.get_rect()
        self.hp = hp

    def move(self, dx: int = 0, dy: int = 0):
        self.rect.x += dx * Wizard.move_speed
        self.rect.y += dy * Wizard.move_speed
