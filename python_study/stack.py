class Stack_lifo:
    def __init__(self,start=[]):
        self.stack = []
        for x in start :
             self.push(x)
    def isEmpty(self):
        return not self.stack
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        if not self.stack:
            print('stack is empty')
        else:
            return self.stack.pop()
            print(self.stack.pop())
    def top(self):
        if not self.stack:
            print('stack is empty')
        else:
            return self.stack[-1]
            print(self.stack[-1])
    def bottom(self):
        if not self.stack:
            print('stack is empty')
        else:
            return self.stack[0]
            print(self.stack[0])
###########################start
cc = Stack_lifo(start=[1,2,3,4,5,6,7])
print(cc.stack)

