#!/usr/bin/python
# -*- coding: utf-8 -*-

class Const:
    def __setattr__(self, key, value):
        if name in self.__dict__:
            raise TypeError("cant change！")
        if not name.isupper():
            raise TypeError("should be upper!")
        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()

print(sys.modules)