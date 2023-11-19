def GameOver():
    print('Will you like to try again?')
    revive = input('Yes or No?')

    if revive.lower() == 'yes':
        treasure_island()
    elif revive.lower() != 'yes':
        print('Game Ended')

def treasure_island():
    print('Welcome to Treasure island')
    direction = input('Go left or right?')

    if (direction).lower() == 'left':
        second_level = input('swim or wait?')

        if second_level.lower() == 'wait':
            third_level = input('Enter the red or yellow or blue door?')

            if third_level.lower() == 'blue':
                print('Eaten by beasts.\nGame Over')
                GameOver()

            elif third_level.lower() == 'red':
                print('Burned by fire.\nGame Over')
                GameOver()

            elif third_level.lower() == 'yellow':
                print('You Win')
                GameOver()

            else:
                print('Game Over')
                GameOver()

        elif second_level.lower() != 'wait': 
            print('Attacked by trout. \nGame Over.')
            GameOver()

    elif direction.lower() != 'left': 
        print('Fall into a hole. \nGame Over.')
        GameOver()

treasure_island()