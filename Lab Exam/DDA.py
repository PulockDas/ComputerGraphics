import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

from InterfaceInit import init

WHITE = (255, 255, 255)

def drawVerticalLine(screen_surface, xStart, yStart, xEnd, yEnd, step):
    if yStart > yEnd:
        temp = yStart
        yStart = yEnd
        yEnd = temp

    y = yStart
    while y < yEnd:
        gfxdraw.pixel(screen_surface, xStart, y, WHITE)
        y = y + step
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawHorizontalLine(screen_surface, xStart, yStart, xEnd, yEnd, step):
    if xStart > xEnd:
        temp = xStart
        xStart = xEnd
        xEnd = temp

    x = xStart
    while x < xEnd:
        gfxdraw.pixel(screen_surface, x, yStart, WHITE)
        x = x + step
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawLineX(screen_surface, xStart, yStart, xEnd, yEnd, m, step):
    if xStart > xEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    x = xStart
    y = yStart
    while x < xEnd:
        gfxdraw.pixel(screen_surface, x, round(y), WHITE)
        x = x+step
        y = y+m*step
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def drawLineY(screen_surface, xStart, yStart, xEnd, yEnd, r_m, step):
    print("drawing line by increasing y")
    if yStart > yEnd:
        xStart, xEnd = xEnd, xStart
        yStart, yEnd = yEnd, yStart

    x = xStart
    y = yStart
    while y < yEnd:
        gfxdraw.pixel(screen_surface, round(x), y, WHITE)
        y = y+step
        x = x+r_m*step
    gfxdraw.pixel(screen_surface, xEnd, yEnd, WHITE)

def DDA(sf, xStart, yStart, xEnd, yEnd, step):
    # screen_surface = sf
    dx = xEnd - xStart
    dy = yEnd - yStart

    if dx == 0:
        drawVerticalLine(sf, xStart, yStart, xEnd, yEnd, step)
        return
    if dy == 0:
        drawHorizontalLine(sf, xStart, yStart, xEnd, yEnd, step)
        return

    m = dy/dx
    if abs(m) <= 1:
        drawLineX(sf, xStart, yStart, xEnd, yEnd, m, step)
    else:
        drawLineY(sf, xStart, yStart, xEnd, yEnd, 1/m, step)
