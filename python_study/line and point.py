import math

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class Line:
    def __init__(self,p1,p2):
        self.x = p1.getx() - p2.getx()
        self.y = p1.gety() - p2.gety()
        self.len = math.sqrt(self.x*self.x+self.y*self.y)
    def getlen(self):
        return self.len

p1 = Point(1,1)
p2 = Point(4,5)
line = Line(p1,p2)
print(line.getlen())