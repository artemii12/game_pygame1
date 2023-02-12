import pygame
from threading import Thread
import pointer_field
import variables
from button import shop_bt_money, shop_bt_attack, shop_bt_protection
from field_with_earnings.object_slot_one import \
    resource_extraction1, resource_extraction2, resource_extraction3
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
                              resource_extraction2(),
                              resource_extraction3())
    text1 = text.text_now(font=font, pos=(WIDTH - 100, 0), colors=[255, 255, 255])

    def creating_platform():
        for i in range(len(rendering)):
            a = randint(0, 30)
            if a == 1:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\coal.png',
                                    serves=2))  # уголь
            elif a == 2:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\copper.png',
                                    serves=1))  # медь
            elif a == 4:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\tin.png',
                                    serves=3))  # олова
            elif a == 5:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\sand.png',
                                    serves=5))  # песок
            elif a == 6:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\flint.png',
                                    serves=6))  # кремень
            elif a == 7:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\iridium.png',
                                    serves=10))  # иридий
            elif a == 8:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\uranium.png',
                                    serves=9))  # уран
            elif a == 9:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\coal.png',
                                    serves=2))  # уголь
            elif a == 10:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\tnt.png',
                                    serves=8))  # тротил
            elif a == 11:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\titan.png',
                                    serves=7))  # титан
            else:
                platform.add(Player((rendering[i][0] * 50), (rendering[i][1]) * 50, colors='img\\ores\\air.png',
                                    serves=0))  # пусто

    th2 = Thread(target=creating_platform())
    th2.start()
    all_sprites.add(FullShopBackground(info=False),
                    ShopBackground(info=False),
                    ShopBackgroundDop(info=False),
                    ShopBackgroundBottom(info=False),
                    ShopBackgroundInfo(info=False))

    all_sprites.add(shop_bt_money(info=False),
                    shop_bt_attack(info=False),
                    shop_bt_protection(info=False))
    all_sprites.add(pointer_field.Point())
    print("the application has started")

    def delet_cu():
        variables.active_menu_point1.clear()
        variables.active_menu_point2.clear()
        variables.active_menu_point3.clear()

    def update_platform(event_list, screen):
        platform.update(event_list)
        platform.draw(screen)



    #  screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    running = True
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:
            if activ_menu_info[0] == 1 and activ_menu_info[1]:
                delet_cu()
                slot_with_information.add(resource_extraction1(),
                                          resource_extraction2(),
                                          resource_extraction3())
                print(activ_menu_info)

            if activ_menu_info[0] == 2 and activ_menu_info[1]:
                delet_cu()
                activ_menu_info[1] = False
                print(activ_menu_info)

            if activ_menu_info[0] == 3 and activ_menu_info[1]:
                delet_cu()
                activ_menu_info[1] = False
                print(activ_menu_info)
            if event.type == pygame.QUIT:
                running = False
            all_sprites.update(event_list)
            slot_with_information.update(event_list)
            text1 = text.text_now(font=font, pos=(WIDTH - 50, 0), colors=[255, 255, 255])
            screen.blit(text1[0], text1[1])

        buttonsGroup.update(event_list, all_sprites, ShopBackground)
        screen.fill('#00E0FF')
        slot_with_information.update(event_list)
        th = Thread(target=update_platform(event_list, screen))
        th.start()
        buttonsGroup.draw(screen)
        all_sprites.draw(screen)
        slot_with_information.draw(screen)
        screen.blit(text1[0], text1[1])
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
