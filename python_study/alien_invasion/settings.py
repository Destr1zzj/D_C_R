#!/usr/bin/python
# -*- coding: utf-8 -*-
class Settings():
    """存储设置的所有类"""

    def __init__(self):
        self.screen_width = 450
        self.screen_height = 800
        self.bg_color = (128,128,128)

        #飞船的设置
        #self.ship_speed_factor = 0.5
        self.ship_limit = 3

        #bullet set  ----start----
        #self.bullet_speed_factor = 0.6
        self.bullet_width = 200
        self.bullet_height = 7
        self.bullet_color = (60,60,60)

        self.bullets_allowed = 2

        #"alien set"
        #self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        # if =1 go right if =-1 go left
        #self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.6
        self.alien_speed_factor = 0.1

        self.fleet_direction = 1
        self.alien_points = 12

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)




    
