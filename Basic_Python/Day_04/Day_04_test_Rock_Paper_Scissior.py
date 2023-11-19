import random

staute =['rock','paper','scissor']
# s > p , p > r , r > s , if equal == draw.

def king_game():
    user_play = int(input('What do you choose?\n0 for Rock \n1 for Paper \n2 for Scissors \n'))
    com_play = random.randint(0,2)
    # print(f"{user_moves} vs {com_moves}")
    
    if user_play >= len(staute):
        print('invalid choice')
        try_again()
    else:
        user_moves = staute[user_play].lower()
        com_moves = staute[com_play].lower()
        print(f"User: {user_moves} \n    vs    \nCom: {com_moves}")

        #we just need take note of what the win condition.
        if user_moves == 'scissor' and com_moves == 'paper':
            print('You Win')
        elif user_moves == 'rock' and com_moves == 'scissor':
            print('You Win')
        elif user_moves == 'paper' and com_moves == 'rock':
            print('You Win')
        elif com_moves == user_moves:
            print('Draw')
            try_again()
        else:
            print('You Lose')
            try_again()


def try_again():
    check = input('Will you wan to try again? \n Y or N \n')

    if check.lower() == 'y':
        king_game()
    else:
        print('Thank you for playing')

king_game()