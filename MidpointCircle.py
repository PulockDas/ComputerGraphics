import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

size = (700, 700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

screen_surface.fill(BLACK)

# Our logic is here
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