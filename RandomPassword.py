import random
import string
length=int(input('Enter the length of the password :'))
strength=input(' Enter the strength of the passsword :').strip()
def random_password_generator(strength):
    if strength=="easy":
        letters=string.ascii_lowercase
        x=''.join(random.choice(letters) for i in range(length))
        return x
    if strength=="hard":
        letters=string.ascii_letters
        x=''.join(random.choice(letters) for i in range(length))
        return x
    if strength == "extreme":
        letters=string.punctuation
        x=''.join(random.choice(letters) for i in range(length))
        return x
    else:
        print(" --Unidentified error--")
password=random_password_generator(strength)
print(" Your password is :", password)
