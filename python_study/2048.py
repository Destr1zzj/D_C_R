#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses
import random
from collections import defaultdict


actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']


actions_dict = dict(zip(letter_codes,actions*2))

def main():
    def init():
       # '''
        #初始化
        #'''
        return 'Game'
    def not_game(state):
       # '''结束界面，退出或者重开'''

        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'

        return responses[actions]

    def game():
        #'''画出当前棋盘状态读取用户输入得到 action'''
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

            if win:
                return 'win'
            if lose:
                return 'game over'
        return 'game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }
    state = 'Init'

    #状态机循环
    while state != 'Exit':
        state = state_actions[state]()

    def get_user_action(keyboard):
        char = 'N'
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]


class GameField(object):
    def __init__(self,height = 4, width = 4, win = 2048):
     #'''初始化棋盘'''
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

    def spwan(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spwan()
        self.spwan()

    
