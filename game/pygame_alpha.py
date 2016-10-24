import pygame
from pygame.locals import *
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("chop")

pikachu = pygame.image.load("pikachu.png").convert()
background = pygame.image.load("bodybg.jpg").convert()
position = pikachu.get_rect()
position.center = width // 2, height // 2

# pikachu.set_colorkey((255, 255, 255))
# pikachu.set_alpha(200)

# print(pikachu.get_at(position.center))

# 设置 opacity
'''
for i in range(position.width):
    for j in range(position.height):
        temp = pikachu.get_at((i, j))
        if temp[3] != 0:
            temp[3] = 20
        pikachu.set_at((i, j), temp)
'''
       
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    
    screen.blit(background, (0, 0))
    # screen.blit(pikachu, position)
    blit_alpha(screen, pikachu, position, 200)
    
    pygame.display.flip()
    clock.tick(30)
