import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy

# 初始化pygame 和 音乐
pygame.init()
pygame.mixer.init()


# 设置游戏背景尺寸， 标题
bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("打飞机 - pygame")

# 载入背景图片
background = pygame.image.load("images/background.png").convert_alpha()

# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def main():
    
    pygame.mixer.music.play(-1)
    
    # 生成我方飞机
    me = myplane.MyPlane(bg_size)
    
    # 用于切换图片
    switch_image = True
    
    # 用于延迟
    delay = 100
    
    running = True
    clock = pygame.time.Clock()
    # 
    
    while running:
        # 退出游戏
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # 检测用户键盘操作
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()
            
                
        # 画屏幕背景
        screen.blit(background, (0, 0))
        
        # 绘制我方飞机
        if switch_image:
            screen.blit(me.image1, me.rect)
        else:
            screen.blit(me.image2, me.rect)
        
        if not(delay % 5):
            switch_image = not switch_image
        
        delay -= 1
        if not delay:
            delay = 100
        
        pygame.display.flip()
        
        # 刷新频率 
        clock.tick(60)
        
            
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
        