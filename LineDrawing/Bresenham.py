import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

from InterfaceInit import init

screen_surface = init("Bresenham's Line Drawing")

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

def bresenhamX(xStart, yStart, xEnd, yEnd, threshold):
    xStart = xStart * threshold
    xEnd = xEnd * threshold

    if xStart > xEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    dx = xEnd - xStart
    dy = yEnd - yStart
    d = 2*dy - dx
    dT = 2*(dy-dx)
    dS = 2*dy

    x = xStart
    y = yStart
    while x<xEnd:
        gfxdraw.pixel(screen_surface, x*threshold, y, WHITE)
        x = x+1
        if d<0:
            d = d + dS
        else:
            y = y+1
            d = d + dT
    gfxdraw.pixel(screen_surface, xEnd*threshold, yEnd, WHITE)

def bresenhamY(xStart, yStart, xEnd, yEnd, threshold):
    print("drawing line by increasing y")
    yStart = yStart * threshold
    yEnd = yEnd * threshold

    if yStart > yEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    dx = xEnd - xStart
    dy = yEnd - yStart
    d = 2 * dx - dy
    dT = 2 * (dx - dy)
    dS = 2 * dx

    x = xStart
    y = yStart
    while y < yEnd:
        gfxdraw.pixel(screen_surface, x, y*threshold, WHITE)
        y = y + 1
        if d < 0:
            d = d + dS
        else:
            x = x + 1
            d = d + dT
    gfxdraw.pixel(screen_surface, xEnd, yEnd*threshold, WHITE)


def display(xStart, yStart, xEnd, yEnd):
    dx = xEnd - xStart
    dy = yEnd - yStart

    if dx == 0:
        drawVerticalLine(xStart, yStart, xEnd, yEnd)
        return
    elif dy == 0:
        drawHorizontalLine(xStart, yStart, xEnd, yEnd)
        return

    m = dy/dx
    if m > 0 and m<1:
        bresenhamX(xStart, yStart, xEnd, yEnd, 1)

    elif m < 0 and m > -1:
        bresenhamX(xStart, xEnd, yStart, yEnd, -1)

    elif m >= 1:
        bresenhamY(xStart, yStart, xEnd, yEnd, 1)
    elif m <= -1:
        bresenhamY(xStart, yStart, xEnd, yEnd, -1)
#

xStart = int(input())
yStart = int(input())
xEnd = int(input())
yEnd = int(input())

display(xStart, yStart, xEnd, yEnd)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()