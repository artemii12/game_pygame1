import pygame
from random import randint
from variables import *
from button import setMenu2

class ShopBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 460))
        self.image.fill("#455D7A")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 200)

class ShopBackgroundAddOnsBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 420))
        self.image.fill("#455D7A")
        self.rect = self.image.get_rect()
        self.rect.center = (210, 220)

    def update(self):
        if not setMenu2:
            self.kill()

