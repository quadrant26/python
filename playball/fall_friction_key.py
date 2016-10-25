import pygame
import sys
import math
from pygame.locals import *
from random import *
from pygame import sprite

'''
set_repeat(delay, interval)
'''

class Ball(pygame.sprite.Sprite):
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)
        
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.side = [choice[-1, 1], choice[-1, 1]]
        self.speed = speed
        self.collide = False
        self.target = target
        self.control = False
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2 
        
    def move(self):
        # 判断是否是电脑控制还是玩家
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move(self.side[0]*self.speed[0], self.side[1]*self.speed[1])
        
        # 如果小球的左侧出了边界， 那么将小球左侧的位置改为右侧的边界
        # 实现左边进入， 右边出来的效果
        if self.rect.right <= 0:
            self.rect.left = self.width
        
        elif self.rect.left >= self.width:
            self.rect.right = 0
        
        elif self.rect.top <= 0:
            self.rect.bottom = self.height
            
        elif self.rect.bottom >= self.height:
            self.rect.top = 0
            
    def check(self, motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False
            
def colide_check(item, target):
    col_balls = [];
    for each in target:
        distance = math.sqrt( math.pow((item.rect.center[0] - each.rect.center[0]), 2) + math.pow((item.rect.center[1] - each.rect.center[1]), 2))
        
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)
            
    return col_balls

class Glass(pygame.sprite.Sprite):
    
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
    
    grayball_image = "gray_ball.png"
    greenball_image = "green_ball.png"
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
    
    # 根据背景图片指定游戏界面的尺寸
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - KING")
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    # 用来存放小球的对象
    balls = []
    group = pygame.sprite.Group()
    
    # 创建 5 个小球
    BALL_NUM = 5
    
    # 创建5个小球
    for i in range(BALL_NUM):
        # 位置随机， 速度随机
        position = randint(0, width-100), randint(0, width-100)
        speed = [randint(10, 10), randint(10, 10)]
        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i + 1))
        # 碰撞检测 ，如果出现碰撞，则重新生成 left top
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, width-100)
        balls.append(ball)
        group.add(ball)
    
    # 实例化摩擦面板
    glass = Glass(glass_image, mouse_image, bg_size)
    
    # 目标
    motion = 0
    
    # 设置自定义事件
    MYTIMER = USEREVENT + 1
    pygame.time.set_time(MYTIMER, 1000)
    
    pygame.key.set_repeat(100, 100)
    
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
                
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0
                    
            elif event.type == MOUSEMOTION:
                motion += 1
                
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1
                            
                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                            
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                
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
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False
                
            if each.control:
                # 画绿色的小球
                screen.blit(each.greenball_image, each.rect)
            else:
                # 画灰色的小球
                screen.blit(each.grayball_image, each.rect)
            
        for each in group:
            group.remove(each)
            
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                '''
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                '''
                # 碰撞之后重新生成速度
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False
                
            group.add(each)
            
        pygame.display.flip()
        clock.tick(30)
        

if __name__ == "__main__":
    main()
        
