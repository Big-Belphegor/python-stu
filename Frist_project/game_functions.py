__author__ = "Alien"
import sys
import pygame

def check_events():
    '''监视键盘和鼠标'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 当鼠标单击关闭键时，执行sys系统命令
            sys.exit()

