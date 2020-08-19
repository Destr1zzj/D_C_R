import random
times = 3
secret = random.randint(1,10)
print('---------start----------')
guess = 0
print ("guess num")
while (guess!=secret)and(times > 0):
    temp = input()
    while not temp.isdigit():
        print("worry")
        temp =  input("another num")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("smart,right")
        print("no gift")
    else:
        if guess > secret:
            print("too big")
        else:
            print("too small")
        if times > 0:
            print("try again")
        else:
            print("no chance")
print("game over")
