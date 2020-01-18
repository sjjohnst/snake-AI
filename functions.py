import pygame as py
import numpy as np
import sys, random

from variables import *
from classes import *

def setGrid(grid):
    for x in range(DIM):
        for y in range(DIM):
            grid.append([x,y])

def eat(snake, apple):
    if snake == apple:
        return True
    return False

def drawGrid(surface):
    for x in range(0, WIDTH, CELLSIZE):
        py.draw.line(surface, GRAY, (x,0), (x,HEIGHT))
        py.draw.line(surface, GRAY, (0,x), (WIDTH,x))

def displayText(message, font):
    surf = font.render(message, True, WHITE)
    rect = surf.get_rect()
    rect.center = (int(WIDTH/2), int(HEIGHT/2))
    return surf, rect
    
def gameOver(basicFont):
    notExit = True
    surf, rect = displayText('GAME OVER', basicFont)

    while notExit:

        for event in py.event.get():
            if event.type == py.QUIT:
                notExit = False
    
            if event.type == py.KEYDOWN:
                notExit = False
        
        py.draw.rect(window, BLACK, rect)
        window.blit(surf, rect)
        py.display.flip()

    return None

def gameWon(basicFont):
    notExit = True
    surf, rect = displayText('YOU WIN', basicFont)

    while notExit:

        for event in py.event.get():
            if event.type == py.QUIT:
                notExit = False
    
            if event.type == py.KEYDOWN:
                notExit = False
        
        py.draw.rect(window, BLACK, rect)
        window.blit(surf, rect)
        py.display.flip()

    return None
    
