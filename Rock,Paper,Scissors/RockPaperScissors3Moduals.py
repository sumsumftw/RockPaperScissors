import time
def results(user_hand,comp_hand):
    if user_hand == "r" or user_hand == "rock":
        if comp_hand == "rock":
            result = "Tied"
        elif comp_hand == "paper":
            result = "Lost"
        else:
            result = "Won"

    if user_hand == "p" or user_hand == "paper":
        if comp_hand == "rock":
            result = "Won"
        elif comp_hand == "paper":
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
    return result

def winCounter(wins,result):
    if result == "Won":
        wins += 1
    return wins

def fullWord(user_hand):
    if len(user_hand) == 1:
        if user_hand == 'r':
            user_hand = 'rock'
        elif user_hand == 'p':
            user_hand = 'paper'
        else:
            user_hand = 'scissors'
    return user_hand

def shoot(hands):
    for i in hands:
        print(f"{i.capitalize()}...")
        time.sleep(1)
    print('Shoot!')
    time.sleep(.3)