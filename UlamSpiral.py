import math
import sys

import pygame
from pygame import QUIT

pygame.init()
pygame.font.init()


my_font = pygame.font.SysFont('Comic Sans MS', 30)

ScreenSize = (700, 700)

screen = pygame.display.set_mode(ScreenSize)

Scale = 1000
Size = (int(ScreenSize[0]*Scale), int(ScreenSize[1]*Scale))
start = False
start1 = False



def find_prime_numbers(range1, o):
    out = []
    for i in range(range1):
        f = False
        if i in o:
            for n in range(2, int(math.sqrt(i)), 1):
                if i % n == 0:
                    f = True
        if not f:
            out.append(i)

    return out


o = find_prime_numbers(Size[0], [])

Up_text = my_font.render('Zooming Out', False, (0, 0, 0))
Down_text = my_font.render('Zooming In', False, (0, 0, 0))


def output_points(center_screen: tuple[int, int], number, scale):
    number = number/scale
    return ((math.cos(number) * number)+center_screen[0]), ((math.sin(number) * number)+center_screen[1])


while True:
    Size = (int(ScreenSize[0] * Scale), int(ScreenSize[1] * Scale))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if start:
                    start = False
                else:
                    start = True
            if event.key == pygame.K_DOWN:
                if start1:
                    start1 = False
                else:
                    start1 = True

    screen.fill((255, 255, 255))

    if start:
        Scale += 0.001
        screen.blit(Up_text, (0, 0))
    if start1:
        Scale -= 0.001
        screen.blit(Down_text, (0, 30))

    if start or start1:
        o = find_prime_numbers(Size[0], o)

    for i in o:
        if i/Size[0] >= 0.005:
            pygame.draw.circle(screen, (0, 0, 0), output_points((int(ScreenSize[0]/2), int(ScreenSize[1]/2)), i, Scale), 1)
    pygame.display.update()






