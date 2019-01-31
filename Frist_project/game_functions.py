__author__ = "Alien"
import sys
import pygame

def check_events():
    '''监视键盘和鼠标'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 当鼠标单击关闭键时，执行sys系统命令
            sys.exit()

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕
    ship.blitme()                       # 将飞船绘制在屏幕上
    pygame.display.flip()               # 让最近绘制的屏幕可见