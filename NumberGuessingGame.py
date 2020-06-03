import random
print(' Welcome to the number guessing game :')
number=random.randint(0,100)
chance=5
while chance!=0:
    guess=int(input(" Enter your guess : "))
    if guess==number:
        print("You won!!")
        break
    if guess>number:
        chance-=1
        print(" Your guess is higher >> ")
    if guess<number:
        chance-=1
        print(" Your guess is lower << ")
else:
    print("The number was : ",number)
    print(" You loose :( ")