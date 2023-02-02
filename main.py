import pygame

import button
from variables import *
from variables import setMenu2
from platform import Player
from shop import ShopBackground, \
                 ShopBackgroundAddOnsBackground
from random import randint
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
all_sprites.add(ShopBackground(), ShopBackgroundAddOnsBackground())
platform = pygame.sprite.Group()
buttonsGroup = pygame.sprite.Group()
buttonsGroup.add(button.bt1(), button.bt2(), button.bt3(), button.bt4())
for i in range(len(rendering1)):
    a = randint(0, 10)
    if a == 5:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#323232'))
    elif a == 3:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#14FFEC'))
    else:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#1FAB89'))

for i in range(len(rendering2)):
    a = randint(0, 10)
    if a == 5:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#323232'))
    elif a == 3:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#14FFEC'))
    else:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#1FAB89'))

font = pygame.font.Font('Samson.ttf', 50)
text = font.render(f'{coin} $', True, [255, 255, 255])
textpos = (HEIGHT+300, 10)
running = True
while running:
    clock.tick(FPS)
    event_list = pygame.event.get()
    for event in event_list:
        if button.setMenu2 and button.on1:
            print(1)
            all_sprites.add(ShopBackgroundAddOnsBackground())
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            button.on1 = False
        if event.type == pygame.QUIT:
            running = False

    platform.update(event_list)
    all_sprites.update()
    buttonsGroup.update(event_list)
    screen.fill('#00E0FF')

    platform.draw(screen)
    all_sprites.draw(screen)
    buttonsGroup.draw(screen)
    screen.blit(text, textpos)
    pygame.display.flip()

pygame.quit()
