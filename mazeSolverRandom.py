import random
import pygame
from pygame import QUIT
import sys
import time

pygame.init()

dict = {}
parentDict = {}

startingIndex = [0, 0]
mase = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0]
]
endingIndex = [3, 3]

screen = pygame.display.set_mode((len(mase[0]) * 50, len(mase) * 50))

point = startingIndex
choices = ['Up', 'Down', 'Left', 'Right']

visited = []
mase[startingIndex[1]][startingIndex[0]] = 2
visited.append(point)

for i in range(len(mase)):
    b = mase[i]
    for u in range(len(b)):
        a = b[u]
        rect1 = pygame.rect.Rect((u * 50), (i * 50), 50, 50)
        if [u, i] == endingIndex:
            pygame.draw.rect(screen, (255, 0, 255), rect1)
        elif a == 0:
            pygame.draw.rect(screen, (0, 0, 255), rect1)
        elif a == 1:
            pygame.draw.rect(screen, (255, 0, 0), rect1)
        elif a == 2:
            pygame.draw.rect(screen, (0, 255, 0), rect1)

pygame.display.update()

time.sleep(3)

backer = []

i = 0
while i < (len(mase) * len(mase[0])) * 4:
    back = False
    choicesCopy = choices[:]
    pointIsh = point[:]
    if point[0] == 0:
        if 'Left' in choicesCopy:
            choicesCopy.remove('Left')
    if point[1] == 0:
        if 'Up' in choicesCopy:
            choicesCopy.remove('Up')
    if point[0] == len(mase[0]) - 1:
        if 'Right' in choicesCopy:
            choicesCopy.remove('Right')
    if point[1] == len(mase) - 1:
        if 'Down' in choicesCopy:
            choicesCopy.remove('Down')
    try:
        if mase[point[1]][point[0] + 1] == 1:
            try:
                choicesCopy.remove('Right')
            except ValueError:
                uybwe = 0
    except IndexError:
        uybwe = 0
    try:
        if mase[point[1] + 1][point[0]] == 1:
            try:
                choicesCopy.remove('Down')
            except ValueError:
                uybwe = 0
    except IndexError:
        uybwe = 0
    if mase[point[1]][point[0] - 1] == 1:
        try:
            choicesCopy.remove('Left')
        except ValueError:
            uybwe = 0
    if mase[point[1] - 1][point[0]] == 1:
        try:
            choicesCopy.remove('Up')
        except ValueError:
            uybwe = 0
    # check if been there
    try:
        if mase[point[1] + 1][point[0] + 0] == 2:
            try:
                choicesCopy.remove('Down')
            except ValueError:
                uybwe = 0
    except IndexError:
        uybwe = 0
    try:
        if mase[point[1] + 0][point[0] + 1] == 2:
            try:
                choicesCopy.remove('Right')
            except ValueError:
                uybwe = 0
    except IndexError:
        uybwe = 0
    if mase[point[1] - 1][point[0] + 0] == 2:
        try:
            choicesCopy.remove('Up')
        except ValueError:
            uybwe = 0
    if mase[point[1] + 0][point[0] - 1] == 2:
        try:
            choicesCopy.remove('Left')
        except ValueError:
            uybwe = 0

    if len(choicesCopy) >= 1:
        if len(choicesCopy) > 1:
            backer.insert(0, point[:])
        choice = random.choice(choicesCopy)

    else:
        point = backer[0]
        backer.remove(backer[0])
        back = True

    if not back:
        if choice == 'Down':
            point[1] += 1
        elif choice == 'Up':
            point[1] -= 1
        elif choice == 'Left':
            point[0] -= 1
        elif choice == 'Right':
            point[0] += 1

        visited.append(point)

    mase[point[1]][point[0]] = 2

    if point == endingIndex:
        print('we did it!!!!!')
        break

    i += 1

for i in range(len(mase)):
    print(f'{mase[i]}')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for i in range(len(mase)):
        b = mase[i]
        for u in range(len(b)):
            a = b[u]
            rect1 = pygame.rect.Rect((u * 50), (i * 50), 50, 50)
            if [u, i] == endingIndex:
                pygame.draw.rect(screen, (255, 0, 255), rect1)
            if a == 0:
                pygame.draw.rect(screen, (0, 0, 255), rect1)
            elif a == 1:
                pygame.draw.rect(screen, (255, 0, 0), rect1)
            elif a == 2:
                pygame.draw.rect(screen, (0, 255, 0), rect1)

    pygame.display.update()