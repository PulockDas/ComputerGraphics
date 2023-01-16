import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

from InterfaceInit import init

screen_surface = init("Midpoint Circle Drawing")

# Our logic is here
WHITE = (255, 255, 255)

def eight_way_symmetric_plot(xc, yc, x, y):
    gfxdraw.pixel(screen_surface, x+xc, y+yc, WHITE)
    gfxdraw.pixel(screen_surface, x+xc, -y+yc, WHITE)
    gfxdraw.pixel(screen_surface, -x+xc, -y+yc, WHITE)
    gfxdraw.pixel(screen_surface, -x+xc, y+yc, WHITE)
    gfxdraw.pixel(screen_surface, y+xc, x+yc, WHITE)
    gfxdraw.pixel(screen_surface, y+xc, -x+yc, WHITE)
    gfxdraw.pixel(screen_surface, -y+xc, -x+yc, WHITE)
    gfxdraw.pixel(screen_surface, -y+xc, x+yc, WHITE)

def display(xc, yc, r):
    x = 0
    y = r
    p = 1-r

    while x <= y:
        eight_way_symmetric_plot(xc, yc, x, y)
        x = x+1

        if p < 0:
            p = p + 2 * x + 1
        else:
            p = p + 2 *(x - y) + 1
            y = y-1

xc = int(input())
yc = int(input())
r = int(input())

display(xc, yc, r)
#

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()