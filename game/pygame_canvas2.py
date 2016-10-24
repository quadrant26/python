import pygame
import sys
from pygame.locals import *

pygame.init()

# 绘制矩形
# reac(surface, color, rect, width=0)
# 绘制多边形
# polygon(sureface, color, pointlist, width=0)

points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Canvas")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen, GREEN, points, 0)
    
    pygame.display.flip()

    clock.tick(10)











