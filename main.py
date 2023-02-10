import pygame

import pointer_field
import variables
from button import shop_bt_money, shop_bt_attack, shop_bt_protection
from field_with_earnings.object_slot_one import \
    resource_extraction1, resource_extraction2
from variables import *
from platform import Player
from shop import ShopBackground, \
    ShopBackgroundDop, ShopBackgroundBottom, \
    FullShopBackground, ShopBackgroundInfo
from random import randint
import text
def main():
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
    text1 = text.text_now(font=font, pos=(WIDTH - 100, 0), colors=[255, 255, 255])

    for i in range(len(rendering1)):
        a = randint(0, 10)
        if a == 5:
            platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, colors='#323232', serves=1)) #  камень
        elif a == 3:
            platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, colors='#14FFEC', serves=2)) #  вода
        else:
            platform.add(Player((rendering1[i][0] * 50), (rendering1[i][1]) * 50, colors='#1FAB89', serves=0)) #  пусто

    for i in range(len(rendering2)):
        a = randint(0, 10)
        if a == 5:
            platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, colors='#323232', serves=1))
        elif a == 3:
            platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, colors='#14FFEC', serves=2))
        else:
            platform.add(Player((rendering2[i][0] * 50), (rendering2[i][1]) * 50, colors='#1FAB89', serves=0))

    all_sprites.add(FullShopBackground(info=False),
                    ShopBackground(info=False),
                    ShopBackgroundDop(info=False),
                    ShopBackgroundBottom(info=False),
                    ShopBackgroundInfo(info=False))

    all_sprites.add(shop_bt_money(info=False),
                    shop_bt_attack(info=False),
                    shop_bt_protection(info=False))
    all_sprites.add(pointer_field.Point())

    def delet_cu():
        variables.active_menu_point1.clear()
        variables.active_menu_point2.clear()
        variables.active_menu_point3.clear()
    print("the application has started")
    #  screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    running = True
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:

            if activ_menu_info[0] == 1 and activ_menu_info[1]:
                delet_cu()
                slot_with_information.add(resource_extraction1(),
                                          resource_extraction2())
                activ_menu_info[1] = False
                print(activ_menu_info)

            if activ_menu_info[0] == 2 and activ_menu_info[1]:
                delet_cu()
                activ_menu_info[1] = False
                print(activ_menu_info)

            if activ_menu_info[0] == 3 and activ_menu_info[1]:
                delet_cu()
                activ_menu_info[1] = False
                print(activ_menu_info)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False
            all_sprites.update(event_list)
            slot_with_information.update(event_list)
            text1 = text.text_now(font=font, pos=(WIDTH - 50, 0), colors=[255, 255, 255])
            screen.blit(text1[0], text1[1])
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


if __name__ == '__main__':
    main()
