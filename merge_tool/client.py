#!/usr/bin/python
# -*- coding: utf-8 -*-
class Cal1():
    def __init__(self):
        self.c = "not nice"

    def calc(self):
        self.c = "nice!"
        return self.c


if __name__ == '__main__':
    a = Cal1()
    a.calc()