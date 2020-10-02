#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import threading
import re

def load_py(path_1 = "D:\\Test_py\\testfile.py", path_2 = "D:\\Test_py\\testfile_2.py", shuxin="123",filename = ""):
    path_1 = path_1
    path_2 = path_2##todo 之后做成读取
    with open(path_1, "r+") as new_f, open(path_2, "r+") as old_f:
            for old_l, new_l in zip(old_f, new_f):
                if old_l == new_l:
                    continue
                elif shuxin in new_l:
                    print('1')
                else:
                    continue


def log():
    print('1')

def change():
    ##mergeshuxing


if __name__ == '__main__':
    load_py()