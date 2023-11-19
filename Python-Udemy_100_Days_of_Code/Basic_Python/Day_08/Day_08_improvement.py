#caesar cipher is anicent encoder.

encrypter = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
should_end =False

def caesar(start_text,shift_amount,cipher_direction):

    encode_message =""
    #encrypt is postive dcrypt is negative
    if cipher_direction == "decode":
        shift_amount *= -1

# need to fix the range so i loop back
    for i in range(len(message)):

        if message[i] in encrypter:
            letter_replace = encrypter.index(message[i]) + shift_amount
            # thinking if i should + 1
            message[i]=encrypter[letter_replace]
            encode_message += message[i]
        else:
            encode_message += message[i]

    print(f'Here\'s the {choice}d result: {encode_message}') 

from art import logo
print(logo)

while not should_end:

    choice = input('Type \'encode\' to encrpty, type \'decode\' to decrypt:\n')
    if choice == 'encode' or choice =='decode':
        message = list(input('Type your message:\n'))
        shifted_num = int(input('Type the shift number:\n'))
        shift = shifted_num % 26
        
        caesar(start_text=message,shift_amount=shift,cipher_direction=choice)
        
        again_ans = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.')

        if again_ans.lower() == 'no':
            should_end = True
            print('Thank you for using the caesar cipher')
    else:
        print('invalid input ')
