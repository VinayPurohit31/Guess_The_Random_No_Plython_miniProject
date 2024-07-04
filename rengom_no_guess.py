import random

def guess(n):
    randonNo=random.randint(0,n)
    guess=0
    while guess!=randonNo:
        guess=int(input(f"Guess the no between 1 to {n}: "))
        if guess > randonNo:
            print("Your guesed is Too High")
        elif guess < randonNo:
            print("Your guesed is Too Low")
    print(f"yeeee Congras You enter no {guess}  is same as the no {randonNo} generated Randomly")

guess(20)