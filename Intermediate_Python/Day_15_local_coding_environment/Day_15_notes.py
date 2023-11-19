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

def check_resources (resources,order,item):
    if order[item]> resources[item]:
        return False
    return True

def subtract_resources(resources,order,item):
    return  resources[item]-order[item]

def add_money(drink_price):
    return +drink_price

money = 0

#alt+shift+click to do mutiple line writing

def startup():
    global money
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
            ingredient = MENU[drink]['ingredients']
            cost_drinks = MENU[drink]['cost']
            
            enough_ingredient = True
            while enough_ingredient:
                # if is True , print missing goods, if is False, continue.
                bool_ingredient = []
                tempt_var = True

                ### This here can be shorter.
                for i in ingredient.keys():
                    tempt_var = check_resources(resources,order = ingredient,item=i)
                    bool_ingredient.append(tempt_var)
                    if tempt_var == False:
                        print(f"There is not enough {i}")
                        enough_ingredient = False
                        startup()

                if sum(bool_ingredient) == len(bool_ingredient):
                    for item in ingredient.keys():
                        resources[item] = subtract_resources(resources,order = ingredient,item=item)
                    # print(f'{resources }have all')
                    enough_ingredient = False

            # print(bool_ingredient[1])
            enough_coin = True
            while enough_coin:
                #insert changes if all is FALSE
                """ Total sum of coins """
                coin_sum = 0
                print('Please insert coins.')
                for i in coin.keys():
                    number = int(input(f"How many {i}?:"))
                    coin_sum += float(format((coin[i]*number),'.2f'))

                # print(f"{coin_sum}")
                if coin_sum > cost_drinks:
                    changes = format((coin_sum - cost_drinks),'.2f')
                    money += add_money(cost_drinks)
                    print(f"Here is ${changes} in changes.")
                    print(f"Enjoy your hot {drink.title()}!")
                    enough_coin = False
                    #enjoy your latte
                    #return to top of chain again
                else:
                    print('Sorry, that not enough money. Money refunded.')
                    #return to coin again
    
startup()
# print(ingredient)
# print(cost_drinks)
# print(resources.keys())