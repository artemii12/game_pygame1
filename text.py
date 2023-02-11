import pygame
import variables

def text_now(font, pos, colors):
    a = 0
    fg = {}
    text = ''
    text2 = []
    for i in variables.resources:
        if variables.resources[i] != 0:
            fg[i] = variables.resources[i]

    for i in fg:
        text2 += f' {i}: {fg[i]} '
    text1 = font.render(text.join(text2), True, colors)

    textpos = (pos[0] - (len(text.join(text2)) * 25), pos[1])
    return text1, textpos


