import variables
import pygame


class resource_extraction(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("#FF2E63")
        self.rect = self.image.get_rect()
        self.rect.center = (variables.WIDTH-325, variables.HEIGHT-255)
        self.click = True


    def urt1(self):

        if self.rect.centerx - 25 < pygame.mouse.get_pos()[0] < self.rect.centerx + 25 and \
                not pygame.mouse.get_pressed()[0]:
            if self.click:
                print(23)
                self.image.fill("#E4F9F5")
                self.click = False
            elif not self.click:
                pass
                """print(12)
                self.image.fill("#FF2E63")
                self.click = True"""

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.urt1()
