#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            # 空栈不能被弹出元素
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 查看栈的栈顶元素（最上面的元素）
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 查看堆栈的最上面的元素
        return not bool(self.stack)#判断栈是否溢

    def size(self):
        # 返回栈的大小
        return len(self.stack)

if __name__ == '__main__':
    str = input(':')
    m = Stack(limit=100)
    for i in str:
        m.push(i)
    print(m.stack)

    for every in range(0,len(m.stack)):
        s = m.pop()
        print(every)
        if every =='(' and s ==')':
            continue
        elif every != '(':
            if s == ')':
                print('ERROR')continue
                break
            else：
