import random

while True:
    choices = [
    'rock',
    'paper',
    'scissor'
    ]

    computer = random.choice(choices)

    player = None


    while player not in choices:
        player = input("Rock, Paper, Scissors: ").lower()


    print("computer: ",computer)


    if computer == player:
      print("it's a tie")
    elif computer == "rock": # rock
        if player == "scissor":
              print("you lose")
        elif player == "paper":
            print("you win")
    elif computer == "paper": # paper
        if player == "scissor":
            print("you win")
        elif player == "rock":
            print("you lose")
    elif computer == "scissor": # scissor
        if player == 'paper':
          print("you lose")
        elif player == 'rock':
         print("you win")


    play_again = input("do you want to play again:(yes/no) ").lower()
    if play_again == "no" or play_again != "yes":
        break

print("bye!")