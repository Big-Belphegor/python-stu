__author__ = "Alien"
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    '''初始化游戏并创建窗口'''

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))    # 窗口大小
    pygame.display.set_caption('Alien Invasion')    # 窗口框内容

    bg_color = (ai_settings.bg_color)               # 定义背景色，RGB格式
    ship = Ship(screen)                             # 创建一个飞船

    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)


run_game()