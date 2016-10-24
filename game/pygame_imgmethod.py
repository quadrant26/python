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
speed = [-2, 1]
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

# 设置放大比例
scale = 1.0

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
                
            # 全屏(F11)
            if event.key == K_F11:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((1366, 768), FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
            
            
            # 放大缩小
            # 放大 + 缩小- 恢复 space
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 最大只能放大一倍， 缩小 50%
                if event.key == K_EQUALS and scale < 2:
                    scale += 0.1
                if event.key == K_MINUS and scale > 0.5:
                    scale -= 0.1
                if event.key == K_SPACE:
                    scale = 1.0
                
                pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width * scale), int(oturtle_rect.height * scale)))
                l_head = turtle
                r_head = pygame.transform.flip(turtle, True, False)
                    
        # 检测窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)
        
        
    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)
