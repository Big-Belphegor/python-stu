__author__ = "Alien"
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_settings,screen):
        '''初始化外新人并设置起始位置'''

        super(Alien, self).__init__()
        self.screen =screen
        self.ai_settings = ai_settings

        # 加载外星人图像并设置rect属性
        self.image = pygame.image.load('images/wxc.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近，外星人位置初始化
        # self.rect.x = self.rect.width
        self.rect.x = 0
        # self.rect.y = self.rect.height
        self.rect.y = 1

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''

        self.screen.blit(self.image,self.rect)