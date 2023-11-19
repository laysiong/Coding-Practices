# def test():
#     return 3 * 2
# test()

sum_value = 0
to_continue = False

#convert this to dictionary.

def math_opertation(math_val,math_opt,math_next_val):
    if math_opt == '*':
        return math_val * math_next_val
    elif math_opt == '/':
        return math_val / math_next_val
    elif math_opt == '+':
        return math_val + math_next_val
    elif math_opt == '-':
        return math_val - math_next_val


while not False:
    if to_continue == True:

        math_val = sum_value
        math_opt = input("+ \n- \n* \n/ \nPick an operation: ")
        math_next_val = float(input("What\'s the next number?: "))

        sum_value = math_opertation(math_val,math_opt,math_next_val)

        print(f'{math_val} {math_opt} {math_next_val} = {sum_value}')

    elif to_continue == False:
        
        math_val = float(input("What\'s the first number?: "))
        math_opt = input("+ \n- \n* \n/ \nPick an operation: ")
        math_next_val = float(input("What\'s the next number?: "))

        sum_value = math_opertation(math_val,math_opt,math_next_val)

        print(f'{math_val} {math_opt} {math_next_val} = {sum_value}')



    next_act= input(f"Type 'y' to continue calculating with {sum_value}, or type 'n' to start a new calculation: ")

    if next_act.lower() == 'y':
        to_continue = True
    elif next_act.lower() == 'n':
        to_continue = False


