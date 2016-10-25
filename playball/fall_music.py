import pygame
import sys
import math
from pygame.locals import *
from random import *

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
            
def main():
    pygame.init()
    
    ball_image = "gray_ball.png"
    bg_image = "background.png"
    
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
    group = pygame.sprite.Group()
    
    # 创建 5 个小球
    BALL_NUM = 5
    
    for i in range(BALL_NUM):
        # 位置随机， 速度随机
        position = randint(0, width-100), randint(0, width-100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        # 碰撞检测 ，如果出现碰撞，则重新生成 left top
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, width-100)
        balls.append(ball)
        group.add(ball)
    
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
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
            
        for each in group:
            group.remove(each)
            
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                
            group.add(each)
            
        pygame.display.flip()
        clock.tick(30)
        

if __name__ == "__main__":
    main()
        
