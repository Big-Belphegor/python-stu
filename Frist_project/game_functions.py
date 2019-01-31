__author__ = "Alien"
import sys
import pygame

def check_keydown_events(event,ship):
    '''按键按下时执行的操作'''

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    '''按键弹起时执行的操作'''

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''监视键盘和鼠标'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 当鼠标单击关闭键时，执行sys系统命令
            sys.exit()

        # elif event.type == pygame.KEYDOWN:        # 此方法为每按一次右键移动一下
        #     # 向右移动飞船
        #     ship.rect.centerx += 1

        elif event.type == pygame.KEYDOWN:          # 此方法为持续或单击都会移动
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings,screen,ship):
    '''初始化窗口状态'''

    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕
    ship.blitme()                       # 将飞船绘制在屏幕上
    pygame.display.flip()               # 让最近绘制的屏幕可见