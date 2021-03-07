#!/usr/bin/python
# -*- coding: utf-8 -*-
class Settings():
    """存储设置的所有类"""

    def __init__(self):
        self.screen_width = 450
        self.screen_height = 800
        self.bg_color = (128,128,128)

        #飞船的设置
        self.ship_speed_factor = 0.5

        #bullet set  ----start----
        self.bullet_speed_factor = 0.6
        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_color = (60,60,60)

        self.bullets_allowed = 2


    
