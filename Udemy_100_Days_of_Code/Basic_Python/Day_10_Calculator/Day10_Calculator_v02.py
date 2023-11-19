def add (a,b):
    return a + b

def minus (a,b):
    return a - b

def mult (a,b):
    return a * b

def divide (a,b):
    return a / b

opertators = {
    '+': add,
    '-': minus,
    '*': mult,
    '/': divide
}



def math_cal():

    math_calculator = True
    math_val = float(input("What\'s the first number?: "))
    for symbol in opertators:
        print(symbol)

    while math_calculator:
    
        math_opt = input("Pick an operation: ")
        math_next_val = float(input("What\'s the next number?: "))
        math_opt_func = opertators[math_opt]
        new_values = math_opt_func(math_val,math_next_val)
        print(f"{math_val}{math_opt}{math_next_val}={new_values}")

        next_act= input(f"Type 'y' to continue calculating with {new_values}, or type 'n' to start a new calculation: ").lower()

        if next_act == 'y':
            math_val=new_values
        else:
            math_calculator = False
            math_cal()


math_cal()
