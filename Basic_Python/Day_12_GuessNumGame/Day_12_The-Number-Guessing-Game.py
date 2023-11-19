# Welcome to the Number Guessing Game

# I'm thinking of a number between 1 and 100.

# Choose a difficulty. Type 'easy' or 'hard'

# hard have 5 attempt
# easy have 10 attempt

# after we guess a number, it return tell us if too high to too low, high or low.
# return how much life we left.

# will you like to run again.

import os
import random

os.system('cls')

print("Welcome to the Number Guessing Game")

#get list of number
List=[]
for i in range(1,101):
    List.append(i)

def check_value (guessing,chosen_num): 
    if guessing > chosen_num:
        return 'Your guess is too high'
    
    elif guessing < chosen_num:
        return 'Your guess is too low'
    
    elif guessing == chosen_num:
        return f'You are correct! The answer was {chosen_num}'
    
def startgame():
    game = True
    play_life = 0

    while game:
        chosen_num = random.choice(List)
        difficulty = str(input("Choose a difficulty. Type \'easy\' or \'hard\' ")).lower()

        if difficulty == 'hard':
            play_life = 5
        elif difficulty == 'easy':
            play_life = 10

        Right_Guess = False

        while not Right_Guess:     
            # print(play_life)

            print(f"You have {play_life} attempts remaing to guess the number.")
            guessing = int(input('Guess the Number '))
            
            print(check_value(guessing,chosen_num))
            play_life -= 1

            if guessing == chosen_num:
                Right_Guess = True
            elif play_life == 0:
                print('You Lose')
                Right_Guess = True
            
        try_again = str(input('will you like to try again? y or n ')).lower()
        if try_again == 'n':
            os.system('cls')
            print('thanks for playing')
            game = False
        elif try_again == 'y':
            os.system('cls')
            game = False
            startgame()

startgame()
    


