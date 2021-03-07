#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from bullet import Bullet


def check_events(ai_settings,screen,ship,bullets):
    #监听键盘和鼠标事件
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit() 
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
        if event.key == pygame.K_RIGHT:
                #向右移动飞船
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            #create bullet
            fire_bullet(event,ai_settings,screen,ship,bullets)
            
def check_keyup_events(event,ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(ai_settings,screen,ship,bullets):
    """刷新屏幕"""
    #每次循环重绘屏幕

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(event,ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        #add bullet in Group
        bullets.add(new_bullet)
