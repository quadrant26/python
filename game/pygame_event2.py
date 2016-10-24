import pygame
# from pygame.locals import *
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("title")
bg = (0, 0, 0)

position = 0
font = pygame.font.Font(None, 20)
line_height = font.get_linesize()
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height
        
        if position > height:
            position = 0
            screen.fill(bg)
            
    pygame.display.flip()