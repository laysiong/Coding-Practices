print('Fizz Buzz Game')
max_num = int(input("Input the max number you will like! \n"))

for i in range (1, max_num+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)