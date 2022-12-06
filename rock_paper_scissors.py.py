import random

a=0
b=0
c=0

while True:
    c+=1
    if c>1:
        print("press 'yes' to play again or press 'no' to end the game.")
        user1=input().lower()
        if user1=='yes':
            choices=['rock','paper','scissors']
            computer=random.choice(choices)
            player=input("rock, paper, or scissors?: ").lower()
            print("computer: ",computer)
            print("player: ",player)
            if player==computer:
                print("Tie.")
            elif (player=='rock' and computer=='paper') or (player=='paper' and computer=='scissors') or (player=='scissors' and computer=='rock'):
                a+=1
                print("you lose")
            elif (player=='rock' and computer=='scissors') or (player=='paper' and computer=='rock') or (player=='scissors' and computer=='paper'):
                b+=1
                print("you win")
            else:
                print("please enter a valid input,")
        elif user1=='no':
            print("so the final score is: CPU = {} ; USER = {}".format(a, b))
            exit()
        else:
            print("please mind your input.")
    else:
        choices = ['rock', 'paper', 'scissors']
        computer = random.choice(choices)
        player = input("rock, paper, or scissors?: ").lower()
        print("computer: ", computer)
        print("player: ", player)
        if player==computer:
            print("Tie.")
        elif (player=='rock' and computer=='paper') or (player=='paper' and computer=='scissors') or (player=='scissors' and computer=='rock'):
            a+=1
            print("you lose")
        elif (player=='rock' and computer=='scissors') or (player=='paper' and computer=='rock') or (player=='scissors' and computer=='paper'):
            b+=1
            print("you win")
        else:
            print("please enter a valid input")