import random
import time

play = "y"
wins = 0

while play == "y":
    hands = ["scissors"]
    possible_inputs = ["r","rock","p","paper","s","scissors"]
    flag = False
    while not flag:
        user_hand = input("Rock, Paper or Scissors?\n"
                          "(Type the word or first letter of your choice.)").lower()
        comp_hand = random.choice(hands)

        if user_hand in possible_inputs:
            flag = True
        else:
            print(f"{user_hand} can not be used!")
            continue

        if user_hand == "r" or user_hand == "rock":
            user_hand = "rock"
            if comp_hand == "rock":
                result = "Tied"
            elif comp_hand == "paper":
                result = "Lost"
            else:
                result = "Won"

        if user_hand == "p" or user_hand == "paper":
            user_hand = "paper"
            if comp_hand == "rock":
                result = "Won"
            elif comp_hand == "paper":
                result = "Tied"
            else:
                result = "Lost"

        if user_hand == "s" or user_hand == "scissors":
            user_hand = "scissors"
            if comp_hand == "Rock":
                result = "Lost"
            elif comp_hand == "Paper":
                result = "Won"
            else:
                result = "Tied"

        for i in hands:
            print(f"{i.capitalize()}...")
            time.sleep(1)
        print(f"Shoot!\n\nYour choice: '{user_hand.capitalize()}'     The computer chose: '{comp_hand.capitalize()}'\nYou have {result}.\n")

        if result == "Won":
            wins += 1
            result = ""

        if result == "Lost":
            print(f"You won {wins} without losing!\n")
            wins = 0
            play = input('If you want to play again type "Y"\nInput anything else to quit!').lower()