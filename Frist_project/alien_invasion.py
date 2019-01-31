__author__ = "Alien"
import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    '''初始化游戏并创建窗口'''

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))    # 窗口大小
    pygame.display.set_caption('Alien Invasion')    # 窗口框内容
    bg_color = (ai_settings.bg_color)               # 定义背景色，RGB格式

    ship = Ship(ai_settings,screen)                 # 创建一个飞船
    alien = Alien(ai_settings,screen)               # 创建一个外星人

    bullets = Group()                               # 创建子弹群组
    aliens = Group()                                # 创建外星人群

    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)



run_game()