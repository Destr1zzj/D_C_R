import tkinter as tk

class app:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()

        self.hi_there = tk.Button(frame,text='123',fg='white').pack()

root = tk.Tk()
app_1 = app(root)

root.mainloop()
