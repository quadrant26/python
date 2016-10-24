import pygame
import sys
from pygame.locals import *
import math as m

pygame.init()

# 绘制矩形
# reac(surface, color, rect, width=1)
# 绘制多边形
# polygon(sureface, color, pointlist, width=1)
# 绘制圆形
# circle(surface, color, pos, radius, width=1)
# 绘制椭圆
# ellipse(surface, color, rect, with=1)
# 绘制弧线
# arc(surface, colot, Rect, start_angle, stop_angle, width=1)
# 绘制线段
# line(surface, color, start_pos, end_pos, width=1)
# lines(surface, color, closed=True/False, pointlist, width=1)
# 抗锯齿
# aaline(surface, color, start_pos, end_pos, blend=1)
# aalines(surface, color, closed=True/False, pointlist, blend=1)

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
    
    pygame.draw.lines(screen, RED, 0, points, 1)
    pygame.draw.line(screen, BLACK, (100, 200), (540, 250), 1)
    
    pygame.draw.aaline(screen, BLACK, (100, 250), (540, 300), 1) # 抗锯齿
    pygame.draw.aaline(screen, BLACK, (100, 300), (540, 350), 0)
    
    pygame.display.flip()

    clock.tick(10)











