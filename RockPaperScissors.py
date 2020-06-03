import  random
while True :
    choice_list = ["rock", "paper", " scissors"]
    computers_choice = random.choice(choice_list)
    users_choice = input(" please enter your choce :").strip()
    if users_choice=='rock'or users_choice=="paper " or users_choice=='scissors':
        if users_choice== computers_choice:
            print(" it's a tie")
            break
        elif users_choice== "rock" and computers_choice == "paper":
            print(" Compputers choice was ", computers_choice)
            print(" you win")
            break
        elif users_choice== "paper" and computers_choice == "rock":
            print(" compputers choice was ", computers_choice)
            print(" you win")
            break
        elif users_choice== "scissors" and computers_choice == "paper":
            print(" compputers choice was ", computers_choice)
            print(" you win")
            break
        elif users_choice== "rock" and computers_choice == "sciisors":
            print(" compputers choice was ", computers_choice)
            print(" you win")
            break
        else:
            print(" compputers choice was ", computers_choice)
            print(' you lose')
            break
    else:
        print(" sorry wrong choice ")
        break





