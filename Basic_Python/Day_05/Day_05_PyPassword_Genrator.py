import random

print('Welcome to PyPassword Generator!')

letters = list('abcdefghijklmnopqrstuvwxyz')
symbols = list('!@#$%^&*()+-')
numbers = list(range(0, 10))

Num_of_letters = int(input('How many letters would you like in your password?\n'))
Num_of_symbols = int(input('How many symbols would you like?\n'))
Num_of_numbers = int(input('How many numbers would you like?\n'))

password = ''
math_random = 0;

for i in range(0,Num_of_letters):
    # password += random.choice(letters) 
    math_random = random.randint(0,Num_of_letters)
    password += letters[math_random]

for i in range(0,Num_of_symbols):
    # password += random.choice(symbols) 
    math_random = random.randint(0,Num_of_symbols)
    password += symbols[math_random]

for i in range(0,Num_of_numbers):
    # password += random.choice(numbers) 
    math_random = random.randint(0,Num_of_numbers)
    password += str(numbers[math_random])

shufflelist = list(password)
random.shuffle(shufflelist)
new_password = ''.join(shufflelist)

print(f"Your password will be {new_password}")
# print(letters)
# print(numbers)
# print(symbols)