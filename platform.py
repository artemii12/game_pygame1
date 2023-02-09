import pygame

from slot_characteristics.slots_for_earning_money import mining_earnings

import variables


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colors, serves):
        pygame.sprite.Sprite.__init__(self)
        self.a = None
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
        self.CHANGE_COLOR = pygame.time.get_ticks()
#  :::::::::::::::::::::::::::::::::::::::::
        self.income = 0
        self.hp = 0
        self.time_out = pygame.time.set_timer(self.CHANGE_COLOR, 1000)
#  :::::::::::::::::::::::::::::::::::::::::



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
                print(variables.coin)
                self.click = False

    def characteristic(self):
        self.a = 0  # какая сейчас ячейка активна
        if variables.activ_menu_info[0] == 1:  # проверка какой слот сейчас
            for i in range(len(variables.active_menu_point1)):
                if variables.active_menu_point1[i]:
                    self.a = i+1
            if self.a == 1:  # какой слот выбран
                save = mining_earnings.object1()  # открытие def для взятие характеристики
                if self.serves == save[3] and variables.coin >= save[0]:
                    """определение вида платформы информация в variables и определение стоимости продукта"""
                    variables.coin -= save[0]
                    self.income = save[2]
                    self.colors = save[4]
                    self.hp = save[5]
                    self.serves = save[6]
            if self.a == 2:  # какой слот выбран
                save = mining_earnings.object2()  # открытие def для взятие характеристики
                if self.serves == save[3] and variables.coin >= save[0]:
                    """определение вида платформы информация в variables и определение стоимости продукта"""
                    variables.coin -= save[0]
                    self.income = save[2]
                    self.colors = save[4]
                    self.hp = save[5]
                    self.serves = save[6]

        if variables.activ_menu_info[0] == 2:
            ...

        if variables.activ_menu_info[0] == 3:
            ...


    def update(self, event_list):
        self.update_pos()
        for event in event_list:
            if event.type == self.CHANGE_COLOR:
                variables.coin += self.income

            self.image.fill(self.colors)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.urt2()
