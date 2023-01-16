import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

from InterfaceInit import init

screen_surface = init("Bresenham's Circle Drawing")

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
    d = 3-2*r
    eight_way_symmetric_plot(xc, yc, x, y)

    while x <= y:
        if d <= 0:
            d = d + (4 * x) + 6
        else:
            d = d + 4 *(x - y) + 10
            y = y-1
        x = x+1
        eight_way_symmetric_plot(xc, yc, x, y)

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