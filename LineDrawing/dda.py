import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

from InterfaceInit import init

screen_surface = init("DDA Line Drawing")

# Our logic is here
WHITE = (255, 255, 255)
def drawVerticalLine(xStart, yStart, xEnd, yEnd):
    if yStart > yEnd:
        temp = yStart
        yStart = yEnd
        yEnd = temp

    y = yStart
    while y < yEnd:
        gfxdraw.pixel(screen_surface, xStart, y, WHITE)
        y = y + 1
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawHorizontalLine(xStart, yStart, xEnd, yEnd):
    if xStart > xEnd:
        temp = xStart
        xStart = xEnd
        xEnd = temp

    x = xStart
    while x < xEnd:
        gfxdraw.pixel(screen_surface, x, yStart, WHITE)
        x = x + 1
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawLineX(xStart, yStart, xEnd, yEnd, m):
    if xStart > xEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    x = xStart
    y = yStart
    while x < xEnd:
        gfxdraw.pixel(screen_surface, x, round(y), WHITE)
        x = x+1
        y = y+m
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawLineY(xStart, yStart, xEnd, yEnd, r_m):
    print("drawing line by increasing y")
    if yStart > yEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    x = xStart
    y = yStart
    while y < yEnd:
        gfxdraw.pixel(screen_surface, round(x), y, WHITE)
        y = y+1
        x = x+r_m
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def display(xStart, yStart, xEnd, yEnd):
    dx = xEnd - xStart
    dy = yEnd - yStart

    if dx == 0:
        drawVerticalLine(xStart, yStart, xEnd, yEnd)
        return
    if dy == 0:
        drawHorizontalLine(xStart, yStart, xEnd, yEnd)
        return

    m = dy/dx
    if abs(m) <= 1:
        drawLineX(xStart, yStart, xEnd, yEnd, m)
    else:
        drawLineY(xStart, yStart, xEnd, yEnd, 1/m)

xStart = int(input())
yStart = int(input())
xEnd = int(input())
yEnd = int(input())

display(xStart, yStart, xEnd, yEnd)
#

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()