__author__ = "Alien"
import pygame

class Ship():
    '''初始化飞船并设置位置'''

    def __init__(self,screen):
        # 初始化飞船位置
        self.screen = screen
        # 移动标志
        self.moving_right = False

        # 加载飞船图片获取其它外界矩形
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将没艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''根据移动标志调整飞船位置'''

        if self.moving_right:
            self.rect.centerx += 1