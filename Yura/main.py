import time
from itertools import count

import pygame
import sys
from time import sleep

from pygame.transform import scale

width = 2000
height = 1100
screen = pygame.display.set_mode((width, height))
pygame.init()
font = pygame.font.Font(None, 36)


def start_game():
    wizard_animation = [pygame.image.load(f'pixil-frame-0 ({i}).png') for i in range(7, 13)]

    class Start(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('pixil-frame-0 (2).png')
            self.rect = self.image.get_rect()
            self.rect.x = width / 2.5
            self.rect.y = height / 3.5

    class Close(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('pixil-frame-0 (3).png')
            self.rect = self.image.get_rect()
            self.rect.x = width / 2.5
            self.rect.y = width / 2.5

    close = Close()
    start = Start()
    pygame.display.set_caption('Shadow Fight')
    screen.fill((123, 93, 54))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if close.rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                elif start.rect.collidepoint(pos):
                    running = False

        screen.fill((123, 93, 54))
        screen.blit(start.image, (start.rect.x, start.rect.y))
        screen.blit(close.image, (close.rect.x, close.rect.y))
        pygame.display.flip()


def you_win():
    win = Win()
    screen.fill((125, 125, 0))
    screen.blit(win.image, (win.rect.x, win.rect.y))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def you_lose():
    lose = Lose()
    screen.fill((125, 125, 0))
    screen.blit(lose.image, (lose.rect.x, lose.rect.y))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def fight_bear():
    wizard_image_load_6 = pygame.image.load('pixil-frame-0 (7).png')
    wizard.image = pygame.transform.scale(wizard_image_load_6, (200, 400))
    wizard.rect = wizard.image.get_rect()
    wizard.rect.x = width / 3
    wizard.rect.y = height / 1.55
    bear.rect.x = width / 1.5
    bear.rect.y = height / 1.3
    bear.hp = 10 * wizard.level
    bear.atk = 3 * wizard.level
    screen.fill((255, 125, 0))
    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
    screen.blit(bear.image, (bear.rect.x, bear.rect.y))
    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
    screen.blit(txt, (width / 1000, height / 1000))
    bear.blit_hp(screen, font)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    purple_ball = Purple_ball()
                    purple_ball.update()
                    screen.fill((255, 125, 0))
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    bear.blit_hp(screen, font)
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(bear.image, (bear.rect.x, bear.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    red_ball = Red_ball()
                    red_ball.update()
                    screen.fill((255, 125, 0))
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    bear.blit_hp(screen, font)
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(bear.image, (bear.rect.x, bear.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
            if wizard.hp <= 0:
                you_lose()
            if bear.hp <= 0:
                wizard.counter += 0.5
                run = False

    wizard.rect_x = width / 2


def fight_spider():
    wizard_image_load_6 = pygame.image.load('pixil-frame-0 (7).png')
    wizard.image = pygame.transform.scale(wizard_image_load_6, (200, 400))
    wizard.rect = wizard.image.get_rect()
    wizard.rect.x = width / 3
    wizard.rect.y = height / 1.55
    spider.rect.x = width / 1.5
    spider.rect.y = height / 1.3
    spider.hp = 13 * wizard.level
    spider.atk = 4 * wizard.level
    screen.fill((255, 125, 0))
    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
    spider.blit_hp(screen, font)
    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
    screen.blit(spider.image, (spider.rect.x, spider.rect.y))
    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
    screen.blit(txt, (width / 1000, height / 1000))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    purple_ball = Purple_ball()
                    purple_ball.update()
                    screen.fill((255, 125, 0))
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    spider.blit_hp(screen, font)
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(spider.image, (spider.rect.x, spider.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    red_ball = Red_ball()
                    red_ball.update()
                    screen.fill((255, 125, 0))
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    spider.blit_hp(screen, font)
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(spider.image, (spider.rect.x, spider.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
            if wizard.hp <= 0:
                you_lose()
            if spider.hp <= 0:
                wizard.counter += 0.5
                run = False

    wizard.rect_x = width / 2


def fight_mantis():
    wizard_image_load_6 = pygame.image.load('pixil-frame-0 (7).png')
    wizard.image = pygame.transform.scale(wizard_image_load_6, (200, 400))
    wizard.rect = wizard.image.get_rect()
    wizard.rect.x = width / 3
    wizard.rect.y = height / 1.55
    mantis.rect.x = width / 1.5
    mantis.rect.y = height / 1.3
    screen.fill((255, 125, 0))
    mantis.blit_hp(screen, font)
    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
    screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
    screen.blit(txt, (width / 1000, height / 1000))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    purple_ball = Purple_ball()
                    purple_ball.update()
                    screen.fill((255, 125, 0))
                    mantis.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    red_ball = Red_ball()
                    red_ball.update()
                    screen.fill((255, 125, 0))
                    mantis.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
            if wizard.hp <= 0:
                you_lose()
            if mantis.hp <= 0:
                wizard.counter += 0.5
                run = False

    wizard.rect_x = width / 2


def fight_wasp():
    wizard_image_load_6 = pygame.image.load('pixil-frame-0 (7).png')
    wizard.image = pygame.transform.scale(wizard_image_load_6, (200, 400))
    wizard.rect = wizard.image.get_rect()
    wizard.rect.x = width / 3
    wizard.rect.y = height / 1.55
    wasp.rect.x = width / 1.5
    wasp.rect.y = height / 1.3
    screen.fill((255, 125, 0))
    wasp.blit_hp(screen, font)
    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
    screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
    screen.blit(txt, (width / 1000, height / 1000))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    purple_ball = Purple_ball()
                    purple_ball.update()
                    screen.fill((255, 125, 0))
                    wasp.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    red_ball = Red_ball()
                    red_ball.update()
                    screen.fill((255, 125, 0))
                    wasp.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
                    txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
                    screen.blit(txt, (width / 1000, height / 1000))
                    pygame.display.flip()
            if wizard.hp <= 0:
                you_lose()
            if wasp.hp <= 0:
                wizard.counter += 0.5
                run = False

    wizard.rect_x = width / 2


def fight_cockroach():
    wizard_image_load_6 = pygame.image.load('pixil-frame-0 (7).png')
    wizard.image = pygame.transform.scale(wizard_image_load_6, (200, 400))
    wizard.rect = wizard.image.get_rect()
    wizard.rect.x = width / 3
    wizard.rect.y = height / 1.55
    cockroach.rect.x = width / 1.5
    cockroach.rect.y = height / 1.3
    screen.fill((255, 125, 0))
    cockroach.blit_hp(screen, font)
    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
    screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    purple_ball = Purple_ball()
                    purple_ball.update()
                    screen.fill((255, 125, 0))
                    cockroach.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
                    pygame.display.flip()
                elif event.key == pygame.K_z:
                    red_ball = Red_ball()
                    red_ball.update()
                    screen.fill((255, 125, 0))
                    cockroach.blit_hp(screen, font)
                    screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
                    screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                    screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
                    pygame.display.flip()
            if wizard.hp <= 0:
                you_lose()
            if cockroach.hp <= 0:
                wizard.counter += 0.5
                run = False

    wizard.rect_x = width / 2
    you_win()


start_game()


class Shadow_fight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 (4).png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 4
        self.rect.y = height / 20


shadow_fight = Shadow_fight()
screen.fill((0, 100, 255))
screen.blit(shadow_fight.image, (shadow_fight.rect.x, shadow_fight.rect.y))
pygame.display.flip()
sleep(3)


class Wizard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_load = pygame.image.load('pixil-frame-0 (7).png')
        self.image_load_2 = pygame.image.load('pixil-frame-0 (9).png')
        self.image_2 = pygame.transform.scale(self.image_load_2, (200, 400))
        self.image = pygame.transform.scale(self.image_load, (200, 400))
        self.rect = self.image.get_rect()
        self.rect.x = width / 2
        self.rect.y = height / 1.55
        self.counter = 1
        self.level = 1
        self.hp = 100
        self.atk_left = 5
        self.atk_right = 3
        self.red_ball_power = 1
        self.txt = font.render(f'хп игрока = {self.hp}', True, (255, 255, 255))
        self.speed = 15

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.level == 6:
                you_win()
            elif self.counter == 1:
                bear.update()
            elif self.counter == 2:
                spider.update()
            elif self.counter == 3:
                mantis.update()
            elif self.counter == 4:
                wasp.update()
            elif self.counter == 5:
                cockroach.update()
            self.image_load_3 = pygame.image.load('pixil-frame-0 (9).png')
            self.image = pygame.transform.scale(self.image_load_3, (200, 400))
            self.rect = self.image.get_rect()
            self.rect.x = width / 2
            self.rect.y = height / 1.55
        else:
            self.image_load_4 = pygame.image.load('pixil-frame-0 (7).png')
            self.image = pygame.transform.scale(self.image_load_4, (200, 400))
            self.rect = self.image.get_rect()
            self.rect.x = width / 2
            self.rect.y = height / 1.55


class Enemy(pygame.sprite.Sprite):
    def __init__(self, base_hp: int = 10):
        super().__init__()
        self.hp = base_hp * wizard.level

    def blit_hp(self, surface: pygame.Surface, m_font: pygame.font.Font):
        surface.blit(m_font.render(f'ХП = {self.hp}', True, (255, 255, 255)), (width / 2, height / 200))

class Bear(Enemy):
    def __init__(self, base_hp: int = 10):
        super().__init__(base_hp)
        self.image_load = pygame.image.load('pixil-frame-0 (29).png')
        self.image = pygame.transform.scale(self.image_load, (600 + wizard.level * 50, 300 + wizard.level * 25))
        self.rect = self.image.get_rect()
        self.rect.x = width / 1.2
        self.rect.y = height / 1.3
        self.atk = 3 * wizard.level

    def update(self):
        self.rect.x -= wizard.speed
        if self.rect.x <= width / 1.8:
            fight_bear()


class Spider(Enemy):
    def __init__(self, base_hp: int = 13):
        super().__init__(base_hp)
        self.image_load = pygame.image.load('pixil-frame-0 (33).png')
        self.image = pygame.transform.scale(self.image_load, (600 + wizard.level * 50, 300 + wizard.level * 25))
        self.rect = self.image.get_rect()
        self.rect.x = width / 1.2
        self.rect.y = height / 1.3
        self.atk = 4 * wizard.level

    def update(self):
        self.rect.x -= wizard.speed
        if self.rect.x <= width / 1.8:
            fight_spider()


class Mantis(Enemy):
    def __init__(self, base_hp: int = 38):
        super().__init__(base_hp)
        self.image_load = pygame.image.load('pixil-frame-0 (34).png')
        self.image = pygame.transform.scale(self.image_load, (600 + wizard.level * 50, 300 + wizard.level * 25))
        self.rect = self.image.get_rect()
        self.rect.x = width / 1.2
        self.rect.y = height / 1.3
        self.atk = 1 * wizard.level

    def update(self):
        self.rect.x -= wizard.speed
        if self.rect.x <= width / 1.8:
            fight_mantis()


class Wasp(Enemy):
    def __init__(self, base_hp: int = 8):
        super().__init__(base_hp)
        self.image_load = pygame.image.load('pixil-frame-0 (35).png')
        self.image = pygame.transform.scale(self.image_load, (600 + wizard.level * 50, 300 + wizard.level * 25))
        self.rect = self.image.get_rect()
        self.rect.x = width / 1.2
        self.rect.y = height / 2.2
        self.atk = 5 * wizard.level

    def update(self):
        self.rect.x -= wizard.speed
        if self.rect.x <= width / 1.8:
            fight_wasp()


class Cockroach(Enemy):
    def __init__(self, base_hp: int = 20):
        super().__init__(base_hp)
        self.image_load = pygame.image.load('pixil-frame-0 (36).png')
        self.image = pygame.transform.scale(self.image_load, (600 + wizard.level * 50, 300 + wizard.level * 25))
        self.rect = self.image.get_rect()
        self.rect.x = width / 1.2
        self.rect.y = height / 1.3888888
        self.atk = 3 * wizard.level

    def update(self):
        self.rect.x -= wizard.speed
        if self.rect.x <= width / 1.8:
            fight_cockroach()


class Win(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 (37).png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 2
        self.rect.y = height / 2


class Lose(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 (38).png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 2
        self.rect.y = height / 2


wizard = Wizard()


class Go_work_desk(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 (28).png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 10
        self.rect.y = height / 2.5


class Back(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('back.png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 10
        self.rect.y = height / 2


class Purple_ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 38().png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 2.5
        self.rect.y = height / 1.3
        self.speed = 30

    def update(self):
        for i in range(20):
            self.rect.x += self.speed
            time.sleep(0.01)
            screen.fill((255, 125, 0))
            screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
            if wizard.counter == 1:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(bear.image, (bear.rect.x, bear.rect.y))
                pygame.display.flip()
            if wizard.counter == 2:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(spider.image, (spider.rect.x, spider.rect.y))
                pygame.display.flip()
            if wizard.counter == 3:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
                pygame.display.flip()
            if wizard.counter == 4:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
                pygame.display.flip()
            if wizard.counter == 5:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
                pygame.display.flip()
            # screen.blit(txt, (width / 1000, height / 1000))
        if wizard.counter == 1:
            bear.hp -= 3
        elif wizard.counter == 2:
            spider.hp -= 3
        elif wizard.counter == 3:
            mantis.hp -= 3
        elif wizard.counter == 4:
            wasp.hp -= 3
        elif wizard.counter == 5:
            cockroach.hp -= 3
        screen.fill((255, 125, 0))
        screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
        screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
        screen.blit(bear.image, (bear.rect.x, bear.rect.y))
        pygame.display.flip()
        wizard.red_ball_power += 1
        # screen.blit(txt, (width / 1000, height / 1000))


class Red_ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pixil-frame-0 (39).png')
        self.rect = self.image.get_rect()
        self.rect.x = width / 2.5
        self.rect.y = height / 1.3
        self.speed = 30

    def update(self):
        for i in range(20):
            self.rect.x += self.speed
            time.sleep(0.01)
            screen.fill((255, 125, 0))
            screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
            if wizard.counter == 1:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(bear.image, (bear.rect.x, bear.rect.y))
                pygame.display.flip()
            if wizard.counter == 2:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(spider.image, (spider.rect.x, spider.rect.y))
                pygame.display.flip()
            if wizard.counter == 3:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
                pygame.display.flip()
            if wizard.counter == 4:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
                pygame.display.flip()
            if wizard.counter == 5:
                screen.blit(self.image, (self.rect.x, self.rect.y))
                screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
                screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
                pygame.display.flip()
            screen.blit(wizard.txt, (width / 1000, height / 1000))
        if wizard.counter == 1:
            bear.hp -= 5 * wizard.red_ball_power
        elif wizard.counter == 2:
            spider.hp -= 5 * wizard.red_ball_power
        elif wizard.counter == 3:
            mantis.hp -= 5 * wizard.red_ball_power
        elif wizard.counter == 4:
            wasp.hp -= 5 * wizard.red_ball_power
        elif wizard.counter == 5:
            cockroach.hp -= 5 * wizard.red_ball_power
        screen.fill((255, 125, 0))
        screen.blit(font.render('BATTLE!', True, (200, 255, 255)), (width / 2, height / 2))
        screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
        screen.blit(bear.image, (bear.rect.x, bear.rect.y))
        wizard.red_ball_power = 1
        txt = font.render(f'хп игрока = {wizard.hp}', True, (255, 255, 255))
        screen.blit(txt, (width / 1000, height / 1000))


go_work_desk = Go_work_desk()
back = Back()
bear = Bear()
spider = Spider()
mantis = Mantis()
wasp = Wasp()
cockroach = Cockroach()
screen.fill((234, 132, 95))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen.fill((255, 255, 255))
                screen.blit(go_work_desk.image, (go_work_desk.rect.x, go_work_desk.rect.y))
                screen.blit(back.image, (back.rect.x, back.rect.y))
                pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if go_work_desk.rect.collidepoint(pos):
                pygame.quit()
                sys.exit()
            elif back.rect.collidepoint(pos):
                screen.fill((234, 132, 95))
        pygame.display.flip()
        if event.type != pygame.KEYDOWN and event.type != pygame.MOUSEMOTION:
            wizard.update()
            screen.fill((234, 132, 95))
            screen.blit(wizard.image, (wizard.rect.x, wizard.rect.y))
            if wizard.counter == 1:
                screen.blit(bear.image, (bear.rect.x, bear.rect.y))
            elif wizard.counter == 2:
                screen.blit(spider.image, (spider.rect.x, spider.rect.y))
            elif wizard.counter == 3:
                screen.blit(mantis.image, (mantis.rect.x, mantis.rect.y))
            elif wizard.counter == 4:
                screen.blit(wasp.image, (wasp.rect.x, wasp.rect.y))
            elif wizard.counter == 5:
                screen.blit(cockroach.image, (cockroach.rect.x, cockroach.rect.y))
            pygame.display.flip()
