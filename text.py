import pygame
from variables import coin
import variables

def text_now(font, text, pos, colors):
    a = 0
    text1 = font.render(text, True, colors)
    for i in range(len(text)):
        a += i
    textpos = (pos[0]-(a*5), pos[1])
    return text1, textpos
