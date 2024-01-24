import random
from RockPaperScissors3Moduals import results,winCounter,fullWord,shoot

play = "y"
wins = 0

while play == "y":
    hands = ["rock","paper","scissors"]
    possible_inputs = ["r","rock","p","paper","s","scissors"]
    flag = False
    while not flag:
        user_hand = input("Rock, Paper or Scissors?\n(Type the word or first letter of your choice.)").lower()
        comp_hand = random.choice(hands)

        if user_hand in possible_inputs:
            flag = True
        else:
            print(f'"{user_hand}" can not be used!')
            continue

        result = results(user_hand,comp_hand)
        user_hand = fullWord(user_hand)

        shoot(hands)
        print(f'Your chose: "{user_hand.capitalize()}"     The computer chose: "{comp_hand.capitalize()}"\nYou have {result}.\n')

        wins = winCounter(wins,result)

        if result == "Lost":
            print(f"You won {wins} without losing!\n")
            wins = 0
            play = input('If you want to play again type "Y".\nType anything else to quit!').lower()