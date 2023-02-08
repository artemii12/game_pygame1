import pygame


from button import shop_bt_money, shop_bt_attack, shop_bt_protection
from field_with_earnings.object_slot_one import \
    resource_extraction1, resource_extraction2
from variables import *
from platform import Player
from shop import ShopBackground, \
    ShopBackgroundDop, shop_background_bottom, FullShopBackground
from random import randint
import text
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
font = pygame.font.Font('Samson.ttf', 50)
all_sprites = pygame.sprite.Group()
slot_with_information = pygame.sprite.Group()
platform = pygame.sprite.Group()
buttonsGroup = pygame.sprite.Group()

slot_with_information.add(resource_extraction1(),
                          resource_extraction2())

for i in range(len(rendering1)):
    a = randint(0, 10)
    if a == 5:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#323232', serves=1)) #  камень
    elif a == 3:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#14FFEC', serves=2)) #  вода
    else:
        platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, '#1FAB89', serves=0)) #  пусто

for i in range(len(rendering2)):
    a = randint(0, 10)
    if a == 5:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#323232', serves=1))
    elif a == 3:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#14FFEC', serves=2))
    else:
        platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, '#1FAB89', serves=0))

all_sprites.add(FullShopBackground(info=False, x=HEIGHT + 260, y=WIDTH - 290),
                ShopBackground(info=False, x=HEIGHT+260, y=WIDTH-290),
                ShopBackgroundDop(info=False, x=HEIGHT+260, y=WIDTH-290),
                shop_background_bottom(info=False, x=HEIGHT+260, y=WIDTH-290))

all_sprites.add(shop_bt_money(info=False, x=HEIGHT+260, y=WIDTH-290),
                shop_bt_attack(info=False, x=HEIGHT+260, y=WIDTH-290),

                shop_bt_protection(info=False, x=HEIGHT+260, y=WIDTH-290))
text1 = text.text_now(font=font, text=f'{coin} $', pos=(WIDTH - 100, 0), colors=[255, 255, 255])
running = True
while running:
    clock.tick(FPS)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(pygame.mouse.get_pos())
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

    screen.blit(text1[0], text1[1])
    pygame.display.flip()

pygame.quit()
