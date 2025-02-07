import pygame
from pygame import QUIT
import math
import sys


ratio = (1, 1)


pygame.init()
screen = pygame.display.set_mode((800, 800))

press = 0
pressed = False

x1 = -10
y1 = -10

x2 = -10
y2 = -10

def segmentPar(pos1: tuple, pos2: tuple, ratio: tuple):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x1-x2
    dy = y1-y2
    return dx * (ratio[1] / (ratio[0] + ratio[1])) + x2, dy * (ratio[1] / (ratio[1] + ratio[0])) + y2


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pressed = True

    screen.fill((0, 0, 0))

    if press == 1:
        x1, y1 = pygame.mouse.get_pos()
        press += 1

    if press == 3:
        x2, y2 = pygame.mouse.get_pos()
        press += 1

    if press == 5:
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)
        pygame.draw.circle(screen, (255, 255, 255), segmentPar((x1, y1), (x2, y2), ratio), 6)

    if press == 6:
        press = 0
        pressed = False

        x1 = -10
        y1 = -10

        x2 = -10
        y2 = -10

    if pressed:
        press += 1
        pressed = False

    pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 6)
    pygame.draw.circle(screen, (255, 255, 255), (x2, y2), 6)

    pygame.display.update()
