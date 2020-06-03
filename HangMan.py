import random
import string
print(" <<welcome to my haangman>>")
x=int(input(" enter the length of the word :"))
letters=string.ascii_lowercase
word=''.join(random.choice(letters) for i in range(x))
print("-"*x)
chance=5 # total no of chnces left by the user
while chance!=0:
    guess=input(" enter the character :")
    c=0
    for i in word:
        if guess == i:
            c+=1
    print('the charcter is present in the word', c, " times")
    chance-=1
y=input(" ENTER YOUR WORD")
if y== word:
    print(" you won the game")
else:
    print(' the word was', word)
    print(" you lose")





