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

opikachu = pygame.image.load("pikachu.jpg")
pikachu = pygame.transform.chop(opikachu, (80, 80, 50, 50))
# pikachu = opikachu
position = pikachu.get_rect()
position.center = width//2, height//2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
        
    
    screen.fill(bg)
    screen.blit(pikachu, position)
    pygame.draw.rect(screen, (0, 0, 0), position, 1)
    
    pygame.display.flip()
    
    clock.tick(30)