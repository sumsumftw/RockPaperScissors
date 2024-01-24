import random
import time

play = "y"

while play == "y":
    hands = ["Rock","Paper","Scissors"]
    comp_hand = random.choice(hands)
    possible_inputs = ["r","rock","p","paper","s","scissors"]
    flag = False
    while not flag:
        user_hand = input("Rock, Paper or Scissors?\n(Type the word or first letter of your choice.)").lower()
        if user_hand in possible_inputs:
            flag = True
        else:
            print(f"{user_hand} can not be used!")
            continue

        if user_hand == "r" or user_hand == "rock":
            if comp_hand == "Rock":
                result = "Tied"
            elif comp_hand == "Paper":
                result = "Lost"
            else:
                result = "Won"

        if user_hand == "p" or user_hand == "paper":
            if comp_hand == "Rock":
                result = "Won"
            elif comp_hand == "Paper":
                result = "Tied"
            else:
                result = "Lost"

        if user_hand == "s" or user_hand == "scissors":
            if comp_hand == "Rock":
                result = "Lost"
            elif comp_hand == "Paper":
                result = "Won"
            else:
                result = "Tied"
        if user_hand == "r":
            user_hand = "rock"
        elif user_hand == "p":
            user_hand = "paper"
        else:
            user_hand = "scissors"
        final_hand = user_hand.capitalize()

        for i in range(3,0,-1):
            print(f"{i}...")
            time.sleep(1)
        print(f"Your choice: '{final_hand}'     The computer chose: '{comp_hand}'\nYou have {result} against the computer.")

        play = input('If you want to play again type "Y"\nType anything else to quit!').lower()

# Single use at a time