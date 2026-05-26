import pygame


class Rendered:
    def __init__(self, screen):
        self.screen = screen

    def draw_all_houses(self, houses_list):
        for house in houses_list:
            one_floor_h = house.fundament * 20 + house.height_window * 20

            for i in range(house.floors):
                for j in range(house.fundament):
                    brick_y = house.rect.y + (i * one_floor_h) + (j * 20)

                    for h in range(house.len_bricks):
                        pygame.draw.rect(self.screen, house.color, (house.rect.x + h * 20, brick_y, 20, 20))

                for j in range(house.height_window):
                    brick_y = house.rect.y + (i * one_floor_h) + (house.fundament * 20) + (j * 20)
                    if j == 0:
                        for h in range(house.len_bricks):
                            pygame.draw.rect(self.screen, house.color, (house.rect.x + h * 20, brick_y, 20, 20))
                    elif j < house.height_window - 1:
                        pygame.draw.rect(self.screen, house.color, (house.rect.x, brick_y, 20, 20))

                        for h in range(1, house.len_bricks - 1):
                            pygame.draw.rect(self.screen, (0, 0, 255), (house.rect.x + h * 20, brick_y, 20, 20))

                        right_wall_x = house.rect.x + (house.len_bricks - 1) * 20
                        pygame.draw.rect(self.screen, house.color, (right_wall_x, brick_y, 20, 20))
                    else:
                        for h in range(house.len_bricks):
                            pygame.draw.rect(self.screen, house.color, (house.rect.x + h * 20, brick_y, 20, 20))
