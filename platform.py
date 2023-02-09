import pygame

from slot_characteristics.slots_for_earning_money import mining_earnings

import variables


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colors, serves):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(colors)
        self.rect = self.image.get_rect()
        self.colors = colors
        self.rect.center = (x, y)
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y
        self.click = True
        self.serves = serves
        self.income = 0
        self.CHANGE_COLOR = pygame.USEREVENT + 1
        self.cl = pygame.time.set_timer(self.CHANGE_COLOR, 1000)

    def update_pos(self):
            if pygame.mouse.get_pressed()[0]:
                variables.the_beginning_of_movement = True
                if self.pos1[0]:
                    self.pos1[1] = pygame.mouse.get_pos()
                    self.pos2 = self.rect.x
                    self.pos3 = self.rect.y
                    self.pos1[0] = False
                else:
                    self.rect.x = -(int(self.pos1[1][0]) - int(pygame.mouse.get_pos()[0]))+int(self.pos2)
                    self.rect.y = -(int(self.pos1[1][1]) - int(pygame.mouse.get_pos()[1])) + int(self.pos3)
            else:
                variables.the_beginning_of_movement = False
                self.pos1 = [True, None]

    def urt1(self):
        if self.rect.centerx-25 < pygame.mouse.get_pos()[0] < self.rect.centerx+25 and \
                not pygame.mouse.get_pressed()[0]:
            if self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25:
                if self.click:
                    self.image.fill("#D7FBE8")
                    self.click = False
                else:
                    self.image.fill("#D7FBE8")
                    self.click = True
        """нажатие левой кнопки мыши"""
    def urt2(self):
        if self.rect.centerx-25 < pygame.mouse.get_pos()[0] < self.rect.centerx+25:
            if self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25:
                self.characteristic()
                print(1)
                self.serves = 5
                variables.setMenu2 = True
                self.click = False

    def characteristic(self):

        if self.serves == 0 and variables.coin >= mining_earnings.cost:
            variables.coin -= mining_earnings.cost
            self.income = mining_earnings.income  # заработок
            self.placement = mining_earnings.placement  # на чем можно размещать этот предмет
            self.colors_now = mining_earnings.colors_now
            self.colors = self.colors_now


    def update(self, event_list):
        for event in event_list:
            if event.type == self.CHANGE_COLOR:
                variables.coin += self.income
            self.update_pos()
            self.image.fill(self.colors)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.urt2()
