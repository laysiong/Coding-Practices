print("Thank you for choosing Python Pizza Deliveries!")
size = input('what size will you like for your pizza? S, M, or L \n')
add_pepperoni = input('Do you want perpperoni? Y or N\n')
extra_cheese = input('Do you want extra cheese? Y or N\n')

bill = 0

if size.upper() == 'S':
    bill +=15
elif size.upper() == 'M':
    bill +=20
elif size.upper() == 'L':
    bill +=25

if add_pepperoni.upper() == 'Y':
    if size.upper() == 'S':
        bill +=2
    else:
        bill +=3

if extra_cheese.upper() =='Y':
    bill +=1

print(f'Thank you for choosing Python Pizza Deliveres. Your final bill is ${bill}')