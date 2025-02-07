import pygame, sys
from pygame.locals import QUIT

scale = 100
posofc = [100, 100]

pygame.init()

screen = pygame.display.set_mode((800, 800))

my_matrix = []
my_matrix.append([1, 1, 1])
my_matrix.append([-1, 1, 1])
my_matrix.append([1, -1, 1])
my_matrix.append([1, 1, -1])
my_matrix.append([-1, -1, 1])
my_matrix.append([1, -1, -1])
my_matrix.append([1, -1, -1])

points = []
point_mat = []
point_rix = []

projection_matrix = [
    [1, 0, 0],
    [0, 1, 0]
]

pro_len = len(projection_matrix)
mat_len = len(my_matrix)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    
    for i in range(mat_len):
        mult1 = my_matrix[i]
        for o in range(pro_len):
            mult2 = projection_matrix[o]
            for u in range(3):
                muu1 = mult1[u]
                muu2 = mult2[u]
                mult3 = muu1*muu2
                points.append(mult3)
            point1 = sum(points)
            point_mat.append(point1)
            points=[]
        point_rix.append(point_mat)
        point_mat=[]
        print(point_rix)
            


    poinnn = len(point_rix)
    for i in range(poinnn):
        poi = point_rix[i]
        poipoi = len(poi)
        for u in range(poipoi):
            x = point_rix[i][0]*100 + 400
            y = point_rix[i][1]*100 + 400
        pygame.draw.circle(screen, (0,0,0), (x,y), 5)
    pygame.display.update()
    #break 

            
