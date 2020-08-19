class Rec:
    length = float(input("long:"))
    width = float(input("wide:"))

    def setrect(self):
        print('enter:')

    def getrect(self):
        print(self.length,self.width)
    def geta(self):
        #return self.width * self.length
        print(self.width * self.length)

new = Rec()

new.getrect()
new.setrect()
new.geta()