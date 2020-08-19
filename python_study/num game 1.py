import random
import easygui as g

g.msgbox("game1")
secret = random.randint(1,10)

msg = "num = ?"
title = "game1"

guess = g.integerbox(msg,title,lowerbound = 1,upperbound = 10)

while True:
    if guess == secret:
        g.msgbox("right")
        break
    else:
        if guess > secret:
            g.msgbox("big")
        else:
            g.msgbox("small")
    guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

g.msgbox("over")