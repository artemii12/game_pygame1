import pygame


from button import shop_bt_money, shop_bt_attack, shop_bt_protection
from field_with_earnings.object_slot_one import resource_extraction
import variables
from variables import *
from platform import Player
from shop import ShopBackground, ShopBackgroundDop
from random import randint

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
slot_with_information = pygame.sprite.Group()
platform = pygame.sprite.Group()
buttonsGroup = pygame.sprite.Group()

slot_with_information.add(resource_extraction())

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

all_sprites.add(ShopBackground(info=False, x=HEIGHT+260, y=WIDTH-290),
                ShopBackgroundDop(info=False, x=HEIGHT+260, y=WIDTH-290))

all_sprites.add(shop_bt_money(info=False, x=HEIGHT+260, y=WIDTH-290),
                shop_bt_attack(info=False, x=HEIGHT+260, y=WIDTH-290),
                shop_bt_protection(info=False, x=HEIGHT+260, y=WIDTH-290))
font = pygame.font.Font('Samson.ttf', 50)
text = font.render(f'{coin} $', True, [255, 255, 255])
textpos = (HEIGHT+300, 10)
running = True
while running:
    clock.tick(FPS)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(pygame.mouse.get_pos())
        if variables.setMenu2:
            print(43)
            variables.menu2_del = False
            all_sprites.update(event_list)
            variables.Menu2_activ = True
            variables.setMenu2 = False
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event_list)
        slot_with_information.update(event_list)


    platform.update(event_list)

    buttonsGroup.update(event_list, all_sprites, ShopBackground)
    screen.fill('#00E0FF')
    slot_with_information.update(event_list)

    platform.draw(screen)
    buttonsGroup.draw(screen)
    all_sprites.draw(screen)
    slot_with_information.draw(screen)
    screen.blit(text, textpos)
    pygame.display.flip()

pygame.quit()
