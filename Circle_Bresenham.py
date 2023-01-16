import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

size = (700, 700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("DDA Line Drawing Algorithm")

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