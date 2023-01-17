import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
from DDA import DDA
from InterfaceInit import init
from MidpointCircle import Midpoint

screen_surface = init("DDA Line Drawing")

# Logic

DDA(screen_surface, 100, 50, 0, 300, 1)
DDA(screen_surface, 0, 300, 100, 300, 10)
DDA(screen_surface, 100, 300, 0, 600, 1)

DDA(screen_surface, 150, 50, 150, 600, 1)
DDA(screen_surface, 150, 600, 250, 600, 1)
DDA(screen_surface, 250, 600, 250, 50, 1)

DDA(screen_surface, 400, 50, 300, 50, 1)
DDA(screen_surface, 300, 50, 300, 300, 1)
DDA(screen_surface, 300, 300, 400, 300, 1)
DDA(screen_surface, 400, 300, 400, 600, 1)
DDA(screen_surface, 400, 600, 300, 600, 1)

DDA(screen_surface, 450, 50, 550, 50, 10)
DDA(screen_surface, 500, 600, 500, 50, 10)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()