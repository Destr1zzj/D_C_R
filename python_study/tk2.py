from tkinter import *

root = Tk()

Girls = ['1','2','3','4','5']
v = []
for i in Girls:
    v.append(IntVar())
    b=Checkbutton(root,text=i,variable = v).pack()


mainloop()
