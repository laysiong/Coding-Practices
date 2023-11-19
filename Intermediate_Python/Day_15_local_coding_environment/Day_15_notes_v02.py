# 3 hot flavors (espresso, Latte, Cappuccino)
# Pricing (1.5 , 2.5 , 3)
# intergrate  (50ml water, 18gcoffee  
            # 200ml water , 24g coffee, 150ml milk
            # 250ml water , 24g coffee, 100ml milk)



#print report what resouse it left and money earned, what have sold

#after order drink, it will reduce our source
#if machine does have enff resource, it will return us which resource is not enough.
#return back to order


#Order
#insert coin
#how many quaters/dimes/nickles/pennis
#if enff mought.

import os
os.system('cls')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 450,
    "coffee": 100,
}

# coins operate (penny 1 cent, Dime 0.10 , nicklel 0.05, quarter 0.25)
coin = {
    'quarters': 0.25,
    'dimes': 0.1,
    'nickles': 0.05,
    'pennies': 0.01,
}

# print(MENU['espresso']['ingredients'])
# print(MENU['espresso']['cost'])

def check_resources (order):
    for item in order:
        if order[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    coin_sum = 0
    print('Please insert coins.')
    for i in coin.keys():
        number = int(input(f"How many {i}?:"))
        coin_sum += float(format((coin[i]*number),'.2f'))
    return coin_sum


def make_coffee(drink,choice_drinks):
    for item in choice_drinks:
        resources[item] -= choice_drinks[item]
    print(f"Here is your {drink} ☕️. Enjoy!")

def is_transaction_successful(payment,drink_cost):
    if payment > drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    print('Sorry, that not enough money. Money refunded.')    
    return False



#alt+shift+click to do mutiple line writing
money = 0
Machine = True

while Machine:
    drink = str(input("What would you like? (Espresso/ Latte/ Cappuccino) ")).lower()
    if drink == "off": 
        Machine = False
    elif drink == "report":
        for i in resources.keys():
            print(f"{i.title()}: {resources[i]}ml")
        print(f"Money: ${money}")
    else:
        choice_drinks = MENU[drink]
        if check_resources(choice_drinks["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment=payment, drink_cost=choice_drinks["cost"]):
                make_coffee(drink, choice_drinks=choice_drinks["ingredients"])


            # print('hello')

    
        # enough_ingredient = True
        # while enough_ingredient:
        #     # if is True , print missing goods, if is False, continue.
        #     bool_ingredient = []
        #     tempt_var = True

            # ### This here can be shorter.
            # for i in ingredient.keys():
            #     tempt_var = check_resources(resources,order = ingredient,item=i)
            #     bool_ingredient.append(tempt_var)
            #     if tempt_var == False:
            #         print(f"There is not enough {i}")
            #         enough_ingredient = False

            # if sum(bool_ingredient) == len(bool_ingredient):
            #     for item in ingredient.keys():
            #         resources[item] = subtract_resources(resources,order = ingredient,item=item)
            #     # print(f'{resources }have all')
            #     enough_ingredient = False

        # # print(bool_ingredient[1])
        # enough_coin = True
        # while enough_coin:
        #     #insert changes if all is FALSE
        #     """ Total sum of coins """
        #     coin_sum = 0
        #     print('Please insert coins.')
        #     for i in coin.keys():
        #         number = int(input(f"How many {i}?:"))
        #         coin_sum += float(format((coin[i]*number),'.2f'))

        #     # print(f"{coin_sum}")
        #     if coin_sum > cost_drinks:
        #         changes = format((coin_sum - cost_drinks),'.2f')
        #         money += add_money(cost_drinks)
        #         print(f"Here is ${changes} in changes.")
        #         print(f"Enjoy your hot {drink.title()}!")
        #         enough_coin = False
        #         #enjoy your latte
        #         #return to top of chain again
        #     else:
        #         print('Sorry, that not enough money. Money refunded.')
        #         #return to coin again
    

# print(ingredient)
# print(cost_drinks)
# print(resources.keys())