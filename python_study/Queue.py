#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node():
    def __init__(self, elem, next=None):
        self.elem = elem  # 表示对应的元素值
        self.next = next  # 表示下一个链接的链点


class Queue(object):
    def __init__(self):
        self.head = None  # 头部链点为 None
        self.rear = None  # 尾部链点为 None

    def is_empty(self):
        return self.head is None  # 判断队列是否为空

    def enqueue(self, elem):
        p = Node(elem)  # 初始化一个新的点
        if self.is_empty():
            self.head = p  # 队列头部为新的链点
            self.rear = p  # 队列尾部为新的链点
        else:
            self.rear.next = p  # 队列尾部的后继是这个新的点
            self.rear = p  # 然后让队列尾部指针指向这个新的点

    def dequeue(self):
        if self.is_empty():  # 判断队列是否为空
            print('Queue_is_empty')  # 若队列为空，则退出 dequeue 操作
        else:
            result = self.head.elem  # result为队列头部元素
            self.head = self.head.next  # 改变队列头部指针位置
            return result  # 返回队列头部元素

    def peek(self):
        if self.is_empty():  # 判断队列是否为空
            print('NOT_FOUND')  # 为空则返回 NOT_FOUND
        else:
            return self.head.elem  # 返回队列头部元素

    def print_queue(self):
        print("queue:")
        temp = self.head
        myqueue = []  # 暂时存放队列数据
        while temp is not None:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


if __name__ == '__main__':
    list1 = Queue()
    list1.enqueue(21)
    list1.enqueue(35)
    list1.enqueue(58)
    list1.enqueue(13)
    print(list1.peek())
    list1.dequeue()
    print(list1.peek())

