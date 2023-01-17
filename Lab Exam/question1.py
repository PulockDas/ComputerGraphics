import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
from DDA import DDA
from InterfaceInit import init
from MidpointCircle import Midpoint

screen_surface = init("DDA Line Drawing")



# logic
DDA(screen_surface, 0, 600, 699, 600, 1)
DDA(screen_surface, 50, 635, 649, 635, 1)
DDA(screen_surface, 100, 670, 599, 670, 10)
DDA(screen_surface, 0, 600, 50, 635, 1)
DDA(screen_surface, 699, 600, 649, 635, 1)
DDA(screen_surface, 50, 635, 100, 670, 10)
DDA(screen_surface, 649, 635, 599, 670, 10)

DDA(screen_surface, 100, 600, 100, 200, 1)
DDA(screen_surface, 100, 200, 200, 200, 1)
DDA(screen_surface, 200, 200, 200, 600, 1)

DDA(screen_surface, 300, 600, 300, 200, 1)
DDA(screen_surface, 300, 200, 330, 100, 1)
DDA(screen_surface, 330, 100, 430, 100, 1)
DDA(screen_surface, 430, 100, 400, 200, 1)
DDA(screen_surface, 400, 200, 400, 600, 1)

DDA(screen_surface, 380, 100, 350, 200, 1)

Midpoint(screen_surface, 350, 400, 40)

DDA(screen_surface, 350, 200, 350, 360, 1)
DDA(screen_surface, 350, 440, 350, 600, 1)

DDA(screen_surface, 599, 600, 599, 200, 1)
DDA(screen_surface, 599, 200, 499, 200, 1)
DDA(screen_surface, 499, 200, 499, 600, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()