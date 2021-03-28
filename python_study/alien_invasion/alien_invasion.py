#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings,screen,stats)

    #设置背景色：
    #bg_color = (128,128,128)

    #create a plane
    ship = Ship(ai_settings,screen)

    #creat alien
    alien = Alien(ai_settings,screen)

    bullets = Group()
    aliens = Group()
    print(aliens)
    gf.create_fleet(ai_settings,screen,ship,aliens)


    #游戏主循环
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,sb,stats)
            gf.update_aliens(ai_settings,aliens,ship,screen,bullets,stats)
        
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb)
            # gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        
run_game()
            


