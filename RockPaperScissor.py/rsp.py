#import the module you will use to simulate the computer's choices:
import random

while True:

    #take the user input
    user_action = input("Enter the choice(rock,paper,scissors):")

    #define the possible choices and let the computer choose on eof them randomly
    possible_actions=["rock", "paper", "scissors"]
    computer_action=random.choice(possible_actions)

    print(f"\nyou choose{user_action}, computer choose{computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}.It's tie!!")
    elif user_action == 'rock':
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("paper covers rock! you loose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! You win.")
        else:
            print("scissors cuts paper! You loose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper! You win.")
        else:
            print("rock smashes scissors! You loose.")
    else:
        print("your choice doesn't exist, You loose")

    play_again = input("play again?(yes/no):")
    if play_again.lower() !="yes":
        break