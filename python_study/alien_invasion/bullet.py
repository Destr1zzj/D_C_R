#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """创建子弹的类"""
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.image = pygame.image.load('alien_invasion\images\\bullet.bmp')
        self.image = pygame.transform.scale(self.image, (200, 7))

        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 

        #save bullet pos as float
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #刷新子弹位置
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在指定位置画bullet"""
        self.screen.blit(self.image,self.rect)




