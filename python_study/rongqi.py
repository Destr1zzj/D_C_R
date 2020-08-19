#!/usr/bin/python
# -*- coding: utf-8 -*-

class Cl:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self .values[key]


class Clist(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self,key):
        self.count[key] += 1
        print(key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super.__setitem__(key,value)

    def __delitem__(self, key):
        del self.count[key]
        super.__delitem__(key)

    def counter(self,key):
        return self.count[key]

    def append(self,value):
        self.count.append(0)
        super().apppend(value)

    def pop(self, key =-1):
        del self.count[key]
        return super().pop(key)

    def remove(self,value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self,key,value):
        self.count.insert(key,0)
        super().insert(key,value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()



