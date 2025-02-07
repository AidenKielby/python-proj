import math
import sys

import pygame
from pygame import QUIT

pygame.init()

screen = pygame.display.set_mode((400, 400))


def TwoDtoThreeD(matrix: list[tuple], camDist: int):
    new = []
    for i in matrix:
        x = i[0] + 2
        y = i[1] + 2
        z = i[2] + 2
        x1 = (x*camDist)/(z+camDist)
        y1 = (y*camDist)/(z+camDist)
        new.append([x1, y1])
    return new


def rotY(deg: float, matrix: list[tuple]):
    new = []
    for i in matrix:
        x = i[0]
        y = i[1]
        z = i[2]
        x1 = x * math.cos(deg) + z * math.sin(deg)
        z1 = -x * math.sin(deg) + z * math.cos(deg)
        new.append((x1, y, z1))
    return new


def rotZ(deg: float, matrix: list[tuple]):
    new = []
    for i in matrix:
        x = i[0]
        y = i[1]
        z = i[2]
        x1 = x * math.cos(deg) - y * math.sin(deg)
        y1 = x * math.sin(deg) + y * math.cos(deg)
        new.append((x1, y1, z))
    return new


def rotX(deg: float, matrix: list[tuple]):
    new = []
    for i in matrix:
        x = i[0]
        y = i[1]
        z = i[2]
        y1 = y * math.cos(deg) - z * math.sin(deg)
        z1 = y * math.sin(deg) + z * math.cos(deg)
        new.append((x, y1, z1))
    return new


Cube = [(1, 1, 1),(1, 1, -1), (1, 1, 1), (1, -1, 1),(1, -1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1), (1, 1, -1)]
Triang = [(0,1,1), (1,0,1), (0,1,1), (-1,0,1), (-1,0,-1),(0,1,-1),(0,1,1),(1,0,1),(1,0,-1),(0,1,-1),(0,1,1),(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1)]

#Cube = Triang

# draw Loop:
while True:
    Cube = rotX(0.0002, Cube)
    Cube = rotY(0.0002, Cube)
    Cube = rotZ(0.0002, Cube)
    D2 = TwoDtoThreeD(Cube, 2000)

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    last = 0
    for i in D2:
        pygame.draw.circle(screen, (0, 0, 0), (i[0]*70, i[1]*70), 5)
        if last != 0:
            pygame.draw.line(screen, (0, 0, 0), last, (i[0]*70, i[1]*70))
        last = (i[0] * 70, i[1] * 70)

    pygame.display.update()


