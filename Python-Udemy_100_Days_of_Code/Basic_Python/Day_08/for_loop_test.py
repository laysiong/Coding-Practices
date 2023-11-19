
# encrypter = list('abcdefghijklmnopqrstuvwxyz')

# message = list(input('Type your message:\n'))
# shifted_num = int(input('Type the shift number:\n'))

# # need to fix the range so i loop back
# for i in range(len(message)):
#     letter_replace = encrypter.index(message[i]) - shifted_num 
#     # thinking if i should + 1

#     if letter_replace > 25 or letter_replace < 0:
#         letter_replace -= 26
    
#     message[i]=encrypter[letter_replace]
#     encode_message = ''.join(message)

#     print(encode_message)
#     print(letter_replace)


# shifted_num = 5
# letter_replace = 0

# for i in range(26):
#     letter_replace += 1
#     letter_replace += shifted_num
    
#     if letter_replace > 26 or letter_replace < 0:
#         letter_replace -= 25

#     print(letter_replace)


test = list('abcdefghijklmnopqrstuvwxyz')

print(test[25] , test[-26])

