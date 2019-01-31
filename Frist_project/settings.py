__author__ = "Alien"
class Settings():
    '''存储所有设置的类'''

    def __init__(self):
        # 屏幕长
        self.screen_width = 1200
        # 屏幕宽
        self.screen_height = 800
        # 屏幕背景色
        self.bg_color = (230,230,230)
        # 每次移动的像素点
        self.ship_speed_factor = 3.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
