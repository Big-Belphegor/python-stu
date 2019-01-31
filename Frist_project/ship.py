__author__ = "Alien"
import pygame

class Ship():
    '''初始化飞船并设置位置'''

    def __init__(self,ai_settings,screen):
        # 初始化飞船位置
        self.screen = screen
        # 设置center中存储小数值
        self.ai_settings = ai_settings
        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 加载飞船图片获取其它外界矩形
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)          # 由于rect只获取整数部分数值所以重新定义一个浮点型属性

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        # 此处用if是为了防止用户同时按住左右键时右键优先级高
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
