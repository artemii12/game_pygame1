import variables
import pygame

class resource_extraction3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/imagic_mining/mining3.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (variables.WIDTH-215, variables.HEIGHT-255)
        self.click = True
        self.active_site = False
        variables.active_menu_point1.append(False)
        for i in range(len(variables.active_menu_point1)):
            self.class_field = i

    def urt1(self):
        if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25 and \
            self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25 and \
                not pygame.mouse.get_pressed()[0]:
            if self.click:
                for i in range(len(variables.active_menu_point1)):
                    if variables.active_menu_point1[i]:
                        variables.active_menu_point1[i] = False
                variables.coord_xy = (self.rect.centerx, self.rect.centery, True)
                variables.active_menu_point1[self.class_field] = True

    def update(self, event_list):
        if variables.activ_menu_info[0] != 1:
            self.kill()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    self.urt1()

class resource_extraction2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/imagic_mining/mining2.png').convert()

        self.rect = self.image.get_rect()
        self.rect.center = (variables.WIDTH-270, variables.HEIGHT-255)
        self.click = True
        self.active_site = False
        variables.active_menu_point1.append(False)
        for i in range(len(variables.active_menu_point1)):
            self.class_field = i

    def urt1(self):
        if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25 and \
            self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25 and \
                not pygame.mouse.get_pressed()[0]:
            if self.click:
                for i in range(len(variables.active_menu_point1)):
                    if variables.active_menu_point1[i]:
                        variables.active_menu_point1[i] = False
                variables.coord_xy = (self.rect.centerx, self.rect.centery, True)
                variables.active_menu_point1[self.class_field] = True

    def update(self, event_list):
        if variables.activ_menu_info[0] != 1:
            self.kill()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    self.urt1()

class resource_extraction1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/imagic_mining/mining1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (variables.WIDTH-325, variables.HEIGHT-255)
        self.click = True
        self.active_site = False
        variables.active_menu_point1.append(False)
        for i in range(len(variables.active_menu_point1)):
            self.class_field = i

    def urt1(self):
        if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25 and \
            self.rect.centery - 25 < pygame.mouse.get_pos()[1] < self.rect.centery + 25 and \
                not pygame.mouse.get_pressed()[0]:
            if self.click:
                for i in range(len(variables.active_menu_point1)):
                    if variables.active_menu_point1[i]:
                        variables.active_menu_point1[i] = False
                variables.coord_xy = (self.rect.centerx, self.rect.centery, True)
                variables.active_menu_point1[self.class_field] = True

    def update(self, event_list):
        if variables.activ_menu_info[0] != 1:
            self.kill()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.urt1()

