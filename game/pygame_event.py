import pygame
# from pygame.locals import *
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("title")

f = open("abc.txt", "w")

while True:
    for event in pygame.event.get():
        f.write(str(event) + "\n")
        
        if event.type == pygame.QUIT:
            f.close();
            sys.exit()
    