import random

def guess(n):
    low=1
    high=n
    responce=''
    while responce!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        responce=input(f'Is your number {guess}? (h)igher, (l)ower, or (c)orrect? ')
        if responce=='h':
            high=guess-1
        elif responce=='l':
            low=guess+1
    print("Yeee your guess was correct!!!")

guess(1000)