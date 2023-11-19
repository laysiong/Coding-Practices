## talk about scope (logcal and global)

## local scope (inside the function)
player_hp = 10

def drinkpotion():
    #this variable is different variable from global scope.
    #this is terrible coding pratice
    player_hp = 8
    print(player_hp)

drinkpotion()
print(player_hp)

## example global scope
player_hp = 10

def drinkpotion():
    potion_str = 2
    print(player_hp)

drinkpotion()
print(player_hp)


##example of using global scope, AVOID modifying global scope.

""" bad coding pratcie
def increase_enemies():
    global enemies
    enemies +=1
    print(enemies)
"""

# this will be better apporach to modify global scope.
def increase_enemies():
    return enemies + 1

def astest():
    enemies = 1

enemies = increase_enemies() #call the funct to increase the global variable 
#keep your global scope CAP and value that are standard, not prom to changes much.

print(enemies)