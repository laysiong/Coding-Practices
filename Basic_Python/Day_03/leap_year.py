year = int(input('what is the year\n'))
leap= 'leap'


if year % 4 == 0:
    leap = 'leap'
    # print('It is a leap year.')
    if year % 100 == 0:
        leap = 'not leap'
        if year % 400 == 0:
            leap = 'leap'
            # print('It is a leap year.')
        else:
            leap = 'not leap'

else:
    leap = 'not leap'

print (f"{year} is {leap} year")