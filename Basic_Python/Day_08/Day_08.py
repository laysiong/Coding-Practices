#caesar cipher is anicent encoder.


encrypter = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')

def encrptation():
    print('ecncrpyed')
    message = list(input('Type your message:\n'))
    shifted_num = int(input('Type the shift number:\n'))

# need to fix the range so i loop back
    for i in range(len(message)):
        letter_replace = encrypter.index(message[i]) + shifted_num 
        # thinking if i should + 1
        message[i]=encrypter[letter_replace]

    encode_message = ''.join(message)
    print(f'Here\'s the encoded result: {encode_message}') 
    go_again()

def decryptopn():
    print('decrptyed')
    message = list(input('Type your message:\n'))
    shifted_num = int(input('Type the shift number:\n'))

# need to fix the range so i loop back
    for i in range(len(message)):
        letter_replace = encrypter.index(message[i]) - shifted_num 
        # thinking if i should + 1
        message[i]=encrypter[letter_replace]

    encode_message = ''.join(message)
    print(f'Here\'s the decoded result: {encode_message}') 
    go_again()


def go_again():
    again_ans = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.')

    if again_ans.lower() == 'yes':
        check_choice ()
    else:
        print('Thank you for using the caesar cipher')


def check_choice ():
    choice = input('Type \'encode\' to encrpty, type \'decode\' to decrypt:\n')
    if choice.lower() == 'encode':
        encrptation()
    elif choice.lower() == 'decode':
        decryptopn()
    else:
        print('invalid input')


check_choice ()
