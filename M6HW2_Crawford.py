#M6HW2 - Random Number Guessing Game
#CTI 110
#Robert Crawford
#11/01/2017

import random


def main():
    
    winning_number = random.randint(1,100)
    while play_game != 'Congratulation, you won!!!':
        guess = int(input('Pick a number from 1-100?'))
        print(play_game(guess,winning_number))

def play_game(guess,winning_number):
    
    if guess > winning_number:
        return "Too high, try again."
    elif guess < winning_number:
        return "Too low, try again."
    else:
        return 'Congratulation, you won!!!'

main()
