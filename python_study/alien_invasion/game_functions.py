#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from bullet import Bullet
from alien import Alien



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

            #快捷推出，可注释
        elif event.key == pygame.K_q:
            sys.exit()

            
def check_keyup_events(event,ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(ai_settings,screen,ship,bullets,aliens):
    """刷新屏幕"""
    #每次循环重绘屏幕

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    

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

def teki_pos():
    import random
    x = float(random.randint(35,415))

    return x


def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 1*alien_width
    number_aliens_x = int(available_space_x/(1.5 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width 
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    '计算y轴有多少机器人'
    available_space_y = (ai_settings.screen_height - (2*alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    "第一行外星人"
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def update_aliens(ai_settings,aliens):
    "检测是否到边缘，并且更新到整群外星人的位置"
    check_fleet_edges(ai_settings,aliens)
    aliens.update()


def check_fleet_edges(ai_settings,aliens):
    #check if is edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    "change direction"
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


        
