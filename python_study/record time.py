#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
class Record:
        def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

        def __get__(self, instance, owner):
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write("[ %s ] 变量于北京时间[ %s ]被读取,%s = %s\n" %
                        (self.name, time.ctime(), self.name, str(self.val)))
            return self.val

        def __set__(self, instance, value):
            filename = "%s_record.txt" % self.name
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write("[ %s ] 变量于北京时间[ %s ]被修改,%s = %s\n" %
                        (self.name, time.ctime(), self.name, str(value )))
                self.val = value

class C:
    y = Record(5,'des')
