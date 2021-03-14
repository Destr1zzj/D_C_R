#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    #设置背景色：
    #bg_color = (128,128,128)

    #create a plane
    ship = Ship(ai_settings,screen)

    #creat alien
    alien = Alien(ai_settings,screen)

    bullets = Group()

    aliens = Group()
    
    gf.create_fleet(ai_settings,screen,ship,aliens)


    #游戏主循环
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        # gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        
run_game()
            


