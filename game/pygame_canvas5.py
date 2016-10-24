import pygame
import sys
from pygame.locals import *
import math as m

pygame.init()

# 绘制矩形
# reac(surface, color, rect, width=0)
# 绘制多边形
# polygon(sureface, color, pointlist, width=0)
# 绘制圆形
# circle(surface, color, pos, radius, width=0)
# 绘制椭圆
# ellipse(surface, color, rect, with=0)
# 绘制弧线
# arc(surface, colot, Rect, start_angle, stop_angle, width=0)

points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Canvas")

position = size[0] // 2, size[1] // 2
moving = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.fill(WHITE)
    
    pygame.draw.arc(screen, RED, (100, 100, 440, 100), 0, m.pi, 1)
    pygame.draw.arc(screen, RED, (220, 50, 200, 200), m.pi, m.pi*2, 1)
    
    pygame.display.flip()

    clock.tick(10)











