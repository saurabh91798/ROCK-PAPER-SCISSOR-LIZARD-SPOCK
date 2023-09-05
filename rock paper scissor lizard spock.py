#ROCK, PAPER, SCISSOR, LIZARD, SPOCK

import random

computer = random.randint(1,5)

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")
player = int(input("Pick a number: "))

if player == 1:
    print("You choose: ", "Rock")
elif player == 2:
    print("You choose: ", "Paper")
elif player == 3:
    print("You choose: ", "Scissors")
elif player == 4:
    print("You choose: ", "Lizard")
else:
    print("You choose: ", "Spock")
    print("Long Live and Prosper")
    

'''
1 for rock
2 for paper
3 for scissors
4 for lizard
5 for spock
'''
if computer == 1:
    print("CPU Choose: ", "Rock")
elif computer == 2:
    print("CPU Choose: ", "Paper")
elif computer == 3:
    print("CPU Choose: ", "Scissors")
elif computer == 4:
    print("CPU Choose: ", "Lizard")
else:
    print("CPU Choose: ", "Spock")
    print("Long Live and Prosper")
    
if player == computer:

    print('It is a tie!')

elif (

        (player == 1 and (computer == 3 or computer == 4))

        or (player == 2 and (computer == 1 or computer == 5))

        or (player == 3 and (computer == 2 or computer == 4))

        or (player == 4 and (computer == 2 or computer == 5))

        or (player == 5 and (computer == 1 or computer == 3))

    ):

    print('You won!')

else:

    print('You lost.')