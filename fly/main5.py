import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy
import bullet

# 初始化pygame 和 音乐
pygame.init()
pygame.mixer.init()


# 设置游戏背景尺寸， 标题
bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("打飞机 - pygame")

# 载入背景图片
background = pygame.image.load("images/background.png").convert_alpha()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)

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


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def main():
    
    pygame.mixer.music.play(-1)
    
    # 生成我方飞机
    me = myplane.MyPlane(bg_size)
    # 生成敌方飞机
    enemies = pygame.sprite.Group()
    
    # 生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # 生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    # 生成敌方小型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)
    
    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
        
    print(bullet1[0])
    
    # 中弹图片索引
    e1_destory_index = 0
    e2_destory_index = 0
    e3_destory_index = 0
    me_destory_index = 0
    
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
        
        # 发射子弹
        if not(delay % 10):
            bullet1[bullet1_index].reset(me.rect.midtop)
            bullet1_index = (bullet1_index + 1) % BULLET1_NUM
        
        # 检测子弹击中敌机
        for b in bullet1:
            if b.active:
                b.move()
                screen.blit(b.image, b.rect)
                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                if enemy:
                    b.active = False
                    for e in enemy_hit:
                        if e in mid_enemies or e in big_enemies:
                            e.hit = True
                            e.energy -= 1
                            if e.energy == 0:
                                e.active = False
                        else:
                            e.active = False
        
        # 绘制大型敌机
        for each in big_enemies:
            # 判断敌机的飞行状态
            if each.active:
                each.move()
                if each.hit:
                    # 绘制打到画面
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
                else:
                    if switch_image:
                        screen.blit(each.image1, each.rect)
                    else:
                        screen.blit(each.image2, each.rect)
                    
                # 绘制血槽
                pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5), (each.rect.right, each.rect.top - 5), 2)
                # 当生命大于 20% 显示绿色
                energy_remain = each.energy / enemy.BigEnemy.energy
                if energy_remain > 0.2:
                    energy_color = GREEN
                else:
                    energy_color = RED
                pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5), (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)
                
                # 即将出现在画面中， 播放音效
                if each.rect.bottom == -50:
                    enemy3_fly_sound.play(-1)
            else: 
                # 毁灭
                if not(delay % 3):
                    if e3_destory_index == 0:
                        enemy3_down_sound.play()
                    screen.blit(each.destory_images[e3_destory_index], each.rect)
                    e3_destory_index = (e3_destory_index + 1) % 6
                    if e3_destory_index == 0:
                        enemy3_fly_sound.stop()
                        each.reset()
                    
        
        # 绘制中型敌机
        for each in mid_enemies:
            if each.active:
                each.move()
                if each.hit:
                    # 绘制打到画面
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
                else:
                    screen.blit(each.image, each.rect)
                
                # 绘制血槽
                pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5), (each.rect.right, each.rect.top - 5), 2)
                # 当生命大于 20% 显示绿色
                energy_remain = each.energy / enemy.MidEnemy.energy
                if energy_remain > 0.2:
                    energy_color = GREEN
                else:
                    energy_color = RED
                pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5), (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)
                
            else:
                # 毁灭
                if e2_destory_index == 0:
                        enemy2_down_sound.play()
                if not(delay % 3):
                    screen.blit(each.destory_images[e2_destory_index], each.rect)
                    e2_destory_index = (e2_destory_index + 1) % 4
                    if e3_destory_index == 0:
                        each.reset()
            
        
        # 绘制小型敌机
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                # 毁灭
                if e1_destory_index == 0:
                        enemy1_down_sound.play()
                if not(delay % 3):
                    screen.blit(each.destory_images[e1_destory_index], each.rect)
                    e1_destory_index = (e1_destory_index + 1) % 4
                    if e3_destory_index == 0:
                        each.reset()
                        
        # 检测我方飞机时候被撞
        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            me.active = False
            for e in enemies_down:
                e.active = False
                
        # 绘制我方飞机
        if me.active:
            if switch_image:
                screen.blit(me.image1, me.rect)
            else:
                screen.blit(me.image2, me.rect)
        else:
            # 毁灭
            if me_destory_index == 0:
                me_down_sound.play()
            if not(delay % 3):
                screen.blit(each.destory_images[me_destory_index], each.rect)
                me_destory_index = (me_destory_index + 1) % 4
                if me_destory_index == 0:
                    # each.reset()
                    print("GAME OVER")
                    running = False
        
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
        
