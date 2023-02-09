import pygame
import variables

class shop_bt_money(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("#30E3CA")
        self.rect = self.image.get_rect()
        self.rect.center = (x+11, y-260)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25:
                        if self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25:
                            variables.activ_menu_info[0] = 1
                            variables.activ_menu_info[1] = True

class shop_bt_attack(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("#30E3CA")
        self.rect = self.image.get_rect()
        self.rect.center = (x+11, y-205)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25:
                        if self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25:
                            variables.activ_menu_info[0] = 2
                            variables.activ_menu_info[1] = True

class shop_bt_protection(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("#30E3CA")
        self.rect = self.image.get_rect()
        self.rect.center = (x+11, y-150)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25:
                        if self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25:
                            variables.activ_menu_info[0] = 3
                            variables.activ_menu_info[1] = True
