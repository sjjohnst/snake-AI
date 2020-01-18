import pygame as py

#DISPLAY
MULTIPLIER = 4
WIDTH = 100 * MULTIPLIER
HEIGHT = 100 * MULTIPLIER

window = window = py.display.set_mode((WIDTH, HEIGHT))

#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (211,211,211)
GREEN = (0,255,0)
RED = (255,0,0)

#GRID SPECS
DIM = 10
CELLSIZE = int(WIDTH / DIM)
COORDINATES = []

#FPS
FPS = 10
fpsLock = py.time.Clock()

#FONTS
basicFontSize = 50
basicFont = 'freesansbold.ttf'
