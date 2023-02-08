import pygame
from variables import coin
import variables

def text_now(font, text, pos, colors):
    text1 = font.render(text, True, colors)
    textpos = pos
    return text1, textpos
