import pygame
import sys
from pygame.locals import *

pygame.init()

# 绘制矩形
# reac(surface, color, rect, width=0)
# 绘制多边形
# polygon(sureface, color, pointlist, width=0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Canvas")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)
    
    pygame.display.flip()

    clock.tick(10)











