import pygame as py
import numpy as np
import sys, random

from variables import *
from functions import *
from classes import *
  
def main():
    
    py.init()

    py.display.set_caption('Snake')
    FONT = py.font.Font(basicFont, basicFontSize)
    
    snake = Snake(0, 0)
    apple = Apple()

    setGrid(COORDINATES)
    #print(COORDINATES)

    path = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3,
            2, 2, 2, 2, 2, 2, 2, 2, 3,
            1, 1, 1, 1, 1, 1, 1, 1, 3,
            2, 2, 2, 2, 2, 2, 2, 2, 3,
            1, 1, 1, 1, 1, 1, 1, 1, 3,
            2, 2, 2, 2, 2, 2, 2, 2, 3,
            1, 1, 1, 1, 1, 1, 1, 1, 3,
            2, 2, 2, 2, 2, 2, 2, 2, 3,
            1, 1, 1, 1, 1, 1, 1, 1, 3,
            2, 2, 2, 2, 2, 2, 2, 2, 2,
            4, 4, 4, 4, 4, 4, 4, 4, 4]
    index = 0

    
    #Game Loop
    while True:
        
        for event in py.event.get():

            if event.type == py.QUIT:

                py.quit()
                sys.exit()

            elif event.type == py.KEYDOWN:

                if event.key == py.K_UP:
                    snake.direction = 4

                elif event.key == py.K_DOWN:
                    snake.direction = 3

                elif event.key == py.K_LEFT:
                    snake.direction = 2
                
                elif event.key == py.K_RIGHT:
                    snake.direction = 1

                elif event.key == py.K_SPACE:
                    snake.grow()
                    apple.update(snake.pieces)

        snake.direction = path[index]
        index += 1;
        if index >= len(path):
            index = 0
        
        window.fill(WHITE)
        
        drawGrid(window)
        apple.draw(window)
        snake.draw(window)
        snake.move()

        if snake.win():
            snake.draw(window)
            gameWon(FONT)
            py.quit()
            sys.exit()
        
        if snake.dead():
            gameOver(FONT)
            py.quit()
            sys.exit()

        if eat(snake.pieces[0], apple.coord):
            snake.grow()
            apple.update(snake.pieces)
        
        py.display.update()
        fpsLock.tick(FPS)

main()
