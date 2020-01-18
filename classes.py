import pygame as py
import numpy as np
import sys, random

from variables import *
from functions import *

class Snake:

    def __init__(self, x=0, y=0, direction=1):
        self.x = x
        self.y = y
        self.w = CELLSIZE
        self.h = CELLSIZE
        self.direction = direction
        self.prevDirection = direction
        self.pieces = [[self.x, self.y]]

    def follow(self, x, y):
        for i in range(len(self.pieces)-1, -1, -1):
            if i == 0:
                head = self.pieces[i]
                head[0] += x*CELLSIZE
                head[1] += y*CELLSIZE
                continue
            else:
                self.pieces[i] = self.pieces[i-1].copy()
    
    def move(self):
        if self.direction == 1 and self.prevDirection != 2:
            self.follow(1,0)
            self.prevDirection = 1
            
        elif self.direction == 2 and self.prevDirection != 1:
            self.follow(-1,0)
            self.prevDirection = 2
            
        elif self.direction == 3 and self.prevDirection != 4:
            self.follow(0,1)
            self.prevDirection = 3
            
        elif self.direction == 4 and self.prevDirection != 3:
            self.follow(0,-1)
            self.prevDirection = 4

    def grow(self):
        newPiece = self.pieces[len(self.pieces)-1].copy()
        self.pieces.append(newPiece)
    
    def draw(self, surface):
        for i in self.pieces:
            x = i[0]
            y = i[1]
            piece = py.Rect(x, y, self.w, self.h)
            py.draw.rect(surface, GREEN, piece)

    def dead(self):
        if self.pieces.count(self.pieces[0]) > 1:
            return True
        x = self.pieces[0][0]
        y = self.pieces[0][1]
        if x >= WIDTH or x < 0:
            return True
        if y >= HEIGHT or y < 0:
            return True

        return False

    def win(self):
        if len(self.pieces) == DIM*DIM:
            return True
        

class Apple:

    def __init__(self, x=0, y=0, coord=[]):
        self.x = random.randrange(0, WIDTH, CELLSIZE)
        self.y = random.randrange(0, HEIGHT, CELLSIZE)
        self.coord = [self.x, self.y]

    def draw(self, surface):
        fruit = py.Rect(self.x,self.y, CELLSIZE, CELLSIZE)
        py.draw.rect(surface, RED, fruit)

    def update(self, notValid):
        while True:
            self.x = random.randrange(0, WIDTH, CELLSIZE)
            self.y = random.randrange(0, HEIGHT, CELLSIZE)
            temp = [self.x, self.y]
            if temp not in notValid:
                break
        self.coord = [self.x, self.y]
