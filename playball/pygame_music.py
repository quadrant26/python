import pygame
import sys
from pygame.locals import *

'''
播放音效
    pygame.mixer.Sound()
        play()                播放音效
        stop()                停止播放
        fadeout()             淡出
        set_volume()          设置音量
        get_volume()          获取音量
        get_num_channels()    播放了多少次
        get_length()          获取该音效的长度  
        get_raw()             将该音效以二进制的格式返回
播放背景音乐
    pygame.mixer.music()
        load()                  载入音乐
        play()    
        rewind()                重新播放
        stop()
        pause()                
        unpause()                恢复播放
        fadeout()        
        set_volumn()
        get_volumn()
        get_busy()               检测音乐流时候正在播放
        set_pos()                设置开始播放的时间
        get_pos()                获取已经播放的时间
        queue()                  将音乐文件放入播放列表中
        set_endevent()           音乐播放完毕时发送事件
        get_endevent()           获取音乐播放完毕时发送的事件类型
'''

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

cat_sound = pygame.mixer.Sound("cat.wav")
cat_sound.set_volume(0.2)
dog_sound = pygame.mixer.Sound("dog.wav")
dog_sound.set_volume(0.2)


bg_size = width, height = 300, 200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Music - KING")

pause = False

pause_img = pygame.image.load("pause.png").convert_alpha()
unpause_img = pygame.image.load("unpause.png").convert_alpha()
pause_rect = pause_img.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width)/2, (height - pause_rect.height)/2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            if event.button == 3:
                dog_sound.play()
                
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
                
    screen.fill((255,255,255))
    
    if pause:
        screen.blit(pause_img, pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_img, pause_rect)
        pygame.mixer.music.unpause()
    
    pygame.display.flip()
    
    clock.tick(30)

















