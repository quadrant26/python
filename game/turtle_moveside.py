import pygame
from pygame.locals import *
import sys

'''
打印支持的分辨率
pygame.display.list_modes()
'''

# 初始化pygame
pygame.init()

size = width, height = 600, 400
speed = [5, 0]
bg = (255, 255, 255)

# 创建指定大小的窗口
screen = pygame.display.set_mode(size, RESIZABLE)
# 设置窗口标题
pygame.display.set_caption("one")

# 加载图片
oturtle = pygame.image.load("pikachu.jpg")
turtle = oturtle
# 获得图像的位置矩形
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

Fullscreen = True

turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle
turtle = turtle_top

# 设置放大比例
scale = 1.0

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == KEYDOWN:
            
            # 全屏(F11)
            if event.key == K_F11:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((1366, 768), FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
        
        
    # 移动图像
    position = position.move(speed)

    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed = [0, 5]
        
    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5, 0]
        
    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0, -5]
        
    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)
