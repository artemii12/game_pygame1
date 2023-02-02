import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colors):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(colors)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
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

    def update(self):
        self.update_pos()
