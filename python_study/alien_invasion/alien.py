#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite
import game_functions

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('alien_invasion\images\\alien.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()


        ##alien first position
        #from game_functions import teki_pos
        # self.rect.centerx = teki_pos() 
        # self.rect.centery = 0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        ##draw
        self.screen.blit(self.image,self.rect)

    