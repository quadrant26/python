import pygame
import sys
import math
from pygame.locals import *
from random import *
from pygame import sprite

'''
spritecollide(sprite, group, dikill, collided=None)
'''

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if self.rect.right < 0:
            self.rect.left = self.width
        
        elif self.rect.left > self.width:
            self.rect.right = 0
        
        elif self.rect.top < 0:
            self.rect.bottom = self.height
            
        elif self.rect.bottom > self.height:
            self.rect.top = 0
            
def colide_check(item, target):
    col_balls = [];
    for each in target:
        distance = math.sqrt( math.pow((item.rect.center[0] - each.rect.center[0]), 2) + math.pow((item.rect.center[1] - each.rect.center[1]), 2))
        
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)
            
    return col_balls

class Glass(pygame, sprite.Sprite):
    
    def __init__(self, glass_image, mouse_image, bg_size):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        
        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) // 2, (bg_size[1] - self.glass_rect.height) // 2
        
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_image.top
        
        # 设置默认鼠标不可见
        pygame.mouse.set_visible(False)
        
        
def main():
    pygame.init()
    
    ball_image = "gray_ball.png"
    bg_image = "background.png"
    glass_image = "glass.png"
    mouse_image = "mouse.png"
    
    # 添加背景音乐
    pygame.mixer.music.load("bg_music.ogg")
    pygame.mixer.music.play()
    
    # 添加音效
    loser_sound = pygame.mixer.Sound("loser.wav")
    laugh_sound = pygame.mixer.Sound("laugh.wav")
    winner_sound = pygame.mixer.Sound("winner.wav")
    hole_sound = pygame.mixer.Sound("hole.wav")
    
    # 音乐播放完毕时游戏结束
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)
    
    running = True
    
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - KING")
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    # 用来存放小球的对象
    balls = []
    
    # 创建 5 个小球
    BALL_NUM = 5
    
    for i in range(BALL_NUM):
        # 位置随机， 速度随机
        position = randint(0, width-100), randint(0, width-100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        # 碰撞检测 ，如果出现碰撞，则重新生成 left top
        while colide_check(ball, balls):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, width-100)
        balls.append(ball)
    
    # 实例化摩擦面板
    glass = Glass(glass_image, mouse_image, bg_size)
    
    clock = pygame.time.Clock()
    
    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False
                
        screen.blit(background, (0, 0))
        screen.blit(glass.glass_image, glass.glass_rect)
        
        # 限定鼠标位置的范围
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.width - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.width - glass.mouse_rect.width    
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.left = glass.glass_rect.top
        if glass.mouse_rect.bottom > glass.glass_rect.height - glass.mouse_rect.height:
            glass.mouse_rect.bottom = glass.glass_rect.height - glass.mouse_rect.height
            
        screen.blit(glass.mouse_image, glass.mouse_rect)
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
        
        # 进行碰撞检测
        for i in range(BALL_NUM):
            item = balls.pop(i)
            
            if colide_check(item, balls):
                item.speed[0] = -item.speed[0] 
                item.speed[1] = -item.speed[1]
                
            balls.insert(i, item)
            
        pygame.display.flip()
        clock.tick(30)
        

if __name__ == "__main__":
    main()
        
