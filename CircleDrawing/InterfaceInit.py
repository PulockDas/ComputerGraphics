import pygame

def init(title):
    pygame.init()

    size = (700, 700)
    screen_surface = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)

    BLACK = (0, 0, 0)

    screen_surface.fill(BLACK)
    return screen_surface