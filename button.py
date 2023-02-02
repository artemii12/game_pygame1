import pygame
from random import randint
from variables import *



class bt1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill("#364F6B")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.click = False

    def update(self, event_list):
        global setMenu2, on
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        if self.click:
                            on = True
                            setMenu2 = False
                            self.click = False
                            print(1)
                        else:
                            print(2)
                            on = True
                            setMenu2 = True
                            self.click = True

class bt2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill("#364F6B")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 160)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        pass

class bt3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill("#364F6B")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 270)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        pass

class bt4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill("#364F6B")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 380)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        pass
on1 = None
setMenu2 = None