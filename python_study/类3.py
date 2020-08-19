class Ticket:
    def __init__(self,weekend = False,child = False):
        self.money = 100
        if weekend:
            self.iuc = 1.2
        else:
            self.inc = 1
        if child:
            self.dis = 0.5
        else:
            self.dis = 1
    def calc_money(self,num):
        return self.money * self.inc * self.dis * num

adult = Ticket()
child = Ticket(child = True)
print (adult.calc_money(2)+child.calc_money(1))
