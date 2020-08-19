#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
# def myGender():
#     print("!!!!")
#     yield 1
#     yield 2
# def myR(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
#
# for i in myR("deszzj"):
#     print (i,end = "")

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3,int(math.sqrt(num)+1),2):
            if num % current == 0:
                return False
        return True
    return False

def get_prime(num):
    while True:
        if is_prime(num):
            yield num
        num += 1

def solve():
    total = 2
    for next_prime in get_prime(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return
    print(total)

if __name__ =='__main__':
    solve()