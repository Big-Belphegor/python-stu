__author__ = "Alien"
import sys
import pygame

def check_events(ship):
    '''监视键盘和鼠标'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 当鼠标单击关闭键时，执行sys系统命令
            sys.exit()

        # elif event.type == pygame.KEYDOWN:        # 此方法为每按一次右键移动一下
        #     # 向右移动飞船
        #     ship.rect.centerx += 1

        elif event.type == pygame.KEYDOWN:          # 此方法为持续或单击都会移动
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕
    ship.blitme()                       # 将飞船绘制在屏幕上
    pygame.display.flip()               # 让最近绘制的屏幕可见