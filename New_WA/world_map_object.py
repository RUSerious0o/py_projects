import pygame


class WorldMapObject(pygame.sprite.Sprite):
    main_image_path = None

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.main_image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.is_in_home = False


class Home(WorldMapObject):
    main_image_path = './images/home_AI.png'
