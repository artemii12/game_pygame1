import pygame
import variables


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((52, 52))
        self.image.fill("#E4F9F5")
        self.rect = self.image.get_rect()
        self.rect.center = (variables.coord_xy[0], variables.coord_xy[1])
        self.click = True
        self.active_site = False

    def update(self, event_list):
        self.rect.center = (variables.coord_xy[0], variables.coord_xy[1])