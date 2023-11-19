import os
os.system('cls')

import random
from game_data import data
from art import logo,vs


#game continue until you got it wrong.
#B be replace always replace A after question (ensure both A and b cannot be the same)
#Compare seen to be random.choice

def rightans (a_num,b_num):
    if a_num > b_num:
        return "A"
    else:
        return "B"

a = random.choice(data)
Game = True
score = 0

print(logo)

while Game:
    b = random.choice(data)
    noduplicate = True

    #to prevent b to same as a
    while noduplicate:
        if b == a:
            b = random.choice(data)
        else:
            noduplicate = False

    right_ans = rightans(a['follower_count'],b['follower_count'])
    
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

    user_ans = str(input("Who has more followers? Type 'A' or 'B'")).upper()
    if user_ans == right_ans: 
        os.system('cls')
        score +=1
        a = b
        print(logo)
        print(f"You're righ! Current score: {score}")

    elif user_ans != right_ans:
        Game = False
        print(f"Your score is {score}. Thank you for playing")



#name, follower_count, description, country
