import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

get_next_card = False

def whowin (player,com):

    if(player == 0):
        print('You win, you got a Blackjack!')
    elif(com == 0):
        print('You lose, Computer got a Blackjack!')
    elif (player > com and player <=21) or (com>21 and player <=21):
        print('You Win')
    elif (com > player and com <=21) or (player>21 and com <=21):
        print('You went over. You lose')
    else:
        print('draw')

def add_score (list):

    if sum(list) == 21 and len(list) ==2:
        return 0
    
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)

    return sum(list)

def assign_card (cards,time,who):
    for i in range(time):
        card_draw = random.randint(0,11)
        who.append(cards[card_draw])
    return who


# test = [10,8]
# print(add_score(test))

# """
def blackjack():
    start_game = str(input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")).lower()

    if start_game == 'y':

        your_card = []
        com_card = []

        #assign card to player and com
        assign_card(cards,time=2,who=your_card)
        assign_card(cards,time=1,who=com_card)

        player_score = add_score(your_card)
        com_score = add_score(com_card)

        print(f"Your cards: {your_card}, current score: {player_score}")
        print(f"Computer's first card: {com_card}")
        get_next_card = True

        while get_next_card:
            want_card = str(input("Type 'y' to get another card, type 'n' to pass: ")).lower()

            if want_card == 'y':
                #you will given a card
                assign_card(cards,time=1,who=your_card)
                player_score = add_score(your_card)
                print(f"Your cards: {your_card}, current score: {player_score}")
                print(f"Computer's first card: {com_card}")

                while com_score !=0 and com_score < 17:
                    #computer will grab a card
                    assign_card(cards,time=1,who=com_card)
                    com_score = add_score(com_card)

                print(f"Your final cards: {your_card}, final score: {player_score}")
                print(f"Computer's final card: {com_card}, , final score: {com_score}")

                #check who win.
                whowin(player=player_score,com=com_score)
                get_next_card = False

            else:
                #computer will grab a card

                while com_score !=0 and com_score < 17:
                    assign_card(cards,time=1,who=com_card)
                    com_score = add_score(com_card)

                print(f"Your final cards: {your_card}, final score: {player_score}")
                print(f"Computer's final card: {com_card}, , final score: {com_score}")
                
                #check who win.
                whowin(player=player_score,com=com_score)
                get_next_card = False

    elif start_game =='n':
        os.system('cls')
        blackjack()

blackjack()
# """