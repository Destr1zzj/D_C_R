#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt

alist = range(5)
it = iter(alist)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

class Year:
    def __init__(self):
        self.now = dt.date.today().year
        print (dt.date.today().year)

    def isrunnian(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isrunnian(self.now):
            self.now -= 1

        temp = self.now
        self .now -= 1
        return temp

c = Year()

for i in c:
    if i >= 2000:
        print(i)
    else:
        break


class MyRev:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

m = MyRev("deszzj")
for i in m:
    print(i,end="")
print(m)
