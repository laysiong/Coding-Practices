import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list) #random.choice(word_list)
Game_condition = False
player_life = 6
display = []

print(logo)
print(chosen_word)

for i in range(len(chosen_word)): 
    display.append('_')


def user_input():
    # global guess # need to lglobal your variable
    guess = input('Guess the words \n').lower()
    print(f"is letter {guess} in words?")
    checkwords(guess)

def checkwords(guess):
    global player_life

    if guess in display:
        print(f"You've already guessed {guess}")

    # to check if the letter in the chosen words    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in display:
        player_life -=1
        print(f'{(guess).upper()} in not chosen word')
    else:
        print(f'{(guess).upper()} is in chosen word!')
    print(display)


while not Game_condition:
    user_input()
    
    if '_' not in display:
        print('you win')
        Game_condition = True
    elif player_life <= 0:
        print('you lost')
        Game_condition = True
        
    print(f'player_life: {player_life}')
    print(stages[player_life])



