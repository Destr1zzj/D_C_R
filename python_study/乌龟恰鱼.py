import random as r

legal_x = [0,10]
legal_y = [0,10]
class Turtle:
    def __init__(self):
        self.power = 100
        # self.x = r.randint(legal_x[0], legal_y[1])
        # self.y = r.randint(legal_y[0], legal_x[1])
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

        #print(self.x,self.y)

    def movet(self):
        step = [1,2,-1,-2]
        new_x = self.x + r.choice(step)
        new_y = self.y + r.choice(step)
        #print("move",new_x,new_y)
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        self.power -= 1

        return (self.x,self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def movef(self):
        step = [1, -1]
        new_x = self.x + r.choice(step)
        new_y = self.y + r.choice(step)
        #print("move", new_x, new_y)
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        return (self.x, self.y)

# me = Turtle()
# me.movet()
# print(me.x,me.y)
# me.movet()
# print(me.x,me.y)
# me.movet()
# print(me.x,me.y)
# me.movet()
# print(me.x,me.y)
# me.movet()
# print(me.x,me.y)
# me.movet()
# print(me.x,me.y)
#MAIN
turtle = Turtle()
fish = []
for i in range(10):
    fish_name = '鱼'+ str(i+1)
    new_fish = Fish()
    fish.append([new_fish,fish_name])
print(fish)
count = 10
while True:
    if len(fish) == 0:
        print("fish all be eaten,game over")
        break
    if turtle.power == 0:
        print("turtle.power = 0 ,game over")
        print("still %d fish" % count)
        break
    pos = turtle.movet()

    for each_fish in fish[:]:#拷贝列表给迭代器，这样不会出错

        if each_fish[0].movef() == pos:
            turtle.eat()
            fish.remove(each_fish)
            count -= 1
            print(each_fish[0].x,each_fish[0].y,'%s在这被吃了' % each_fish[1])
