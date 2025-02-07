import pygame
from pygame import QUIT
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))

planetMass = 200
sunMass = 600
gravitationalConstant = 6.6743 * math.pow(10, -6)
planetRadius = 10
sunRadius = 50
timestamp = 40
planetVelocityVector = [0, 0.00325]
planetX = 700
planetY = 400
posVector = (planetX, planetY)
positions = [(planetX, planetY)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (int(posVector[0]), int(posVector[1])), planetRadius)
    pygame.draw.circle(screen, (200, 200, 0), (400, 400), sunRadius)

    dx = 400 - posVector[0]
    dy = 400 - posVector[1]
    distance = math.sqrt(dx**2 + dy**2)

    planetForce = gravitationalConstant * (planetMass * sunMass) / (distance**2)

    normalizedVector = [dx / distance, dy / distance]

    accelerationVector = [planetForce * normalizedVector[0] / planetMass, planetForce * normalizedVector[1] / planetMass]

    planetVelocityVector[0] += accelerationVector[0] * timestamp
    planetVelocityVector[1] += accelerationVector[1] * timestamp

    posVector = (posVector[0] + planetVelocityVector[0] * timestamp, posVector[1] + planetVelocityVector[1] * timestamp)

    if math.sqrt((positions[-1][0]-posVector[0])**2 + (positions[-1][1]-posVector[1])**2) > 10:
        if len(positions) < 50:
            positions.append(posVector)
        else:
            del positions[0]
            positions.append(posVector)

    for i in positions:
        pygame.draw.circle(screen, (100, 100, 100), (int(i[0]), int(i[1])), planetRadius-5)

    pygame.display.update()

