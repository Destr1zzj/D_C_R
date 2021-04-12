#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import time
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化飞船和位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('alien_invasion\images\ship.png')
        self.image = pygame.transform.scale(self.image, (70, 54))
        self.rect = self.image.get_rect()
        #print(self.rect.right)
        self.screen_rect = screen.get_rect()
        #print(self.screen_rect.right)

        #将飞船放到初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #center 存储小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
    def update(self):
        "根据移动标志调整位置"

        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.centery > 0:
            self.centery -= self.ai_settings.ship_speed_factor    
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """在指定位置画飞机"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        print(self.centerx,self.centery )
        self.centerx = self.screen_rect.centerx
        
        self.centery = self.screen_rect.bottom -25
        print(self.centerx,self.centery )