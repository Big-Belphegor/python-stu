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
