import pygame
import variables

class ShopButtonExit(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image.fill("#11999E")
        self.rect = self.image.get_rect()
        self.rect.center = (x+15, y-210)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update_pos(self):
        if pygame.mouse.get_pressed()[0]:
            if self.pos1[0]:
                self.pos1[1] = pygame.mouse.get_pos()
                self.pos2 = self.rect.x
                self.pos3 = self.rect.y
                self.pos1[0] = False
            else:
                self.rect.x = -(int(self.pos1[1][0]) - int(pygame.mouse.get_pos()[0]))+int(self.pos2)
                self.rect.y = -(int(self.pos1[1][1]) - int(pygame.mouse.get_pos()[1])) + int(self.pos3)
        else:
            self.pos1 = [True, None]

    def fording(self):
        if variables.Menu2_activ:
            if self.rect.centerx-25 < pygame.mouse.get_pos()[0] < self.rect.centerx+25:
                if self.rect.centery - 12 < pygame.mouse.get_pos()[1] < self.rect.centery + 12:

                    variables.Menu2_activ = False
                    variables.coord_XY = ()

                    variables.menu2_del = True

    def update(self, event_list):
        for event in event_list:
            self.update_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.fording()
            if variables.menu2_del:
                self.kill()

            variables.setMenu2 = False

class ShopBackground(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((62, 300))
        self.image.fill("#455D7A")
        self.rect = self.image.get_rect()
        self.rect.center = (x+13, y-150)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update(self, event_list):
        for event in event_list:
            pass

class ShopBackgroundDop(pygame.sprite.Sprite):
    def __init__(self, info, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 300))
        self.image.fill("#455D7A")
        self.rect = self.image.get_rect()
        self.rect.center = (x-170, y-150)
        self.activ = info
        self.pos1 = [True, None]
        self.pos2 = self.rect.x
        self.pos3 = self.rect.y

    def update(self, event_list):
        for event in event_list:
            pass
