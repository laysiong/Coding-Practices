# for key in dictionary
#   print(key)
#   print(dict[key])
import os

print('Welcome to the sceret relic acution program.')

bid_list = []
bid_status =False

highest = 0
keep = []
while not bid_status:

    bid_name = str(input('What is your name?: '))
    bid_amt = float(input('What\'s your bid? :$'))
    
    bid_dict = {}

    bid_dict['Name'] = bid_name
    bid_dict['Amount'] = bid_amt
    bid_list.append(bid_dict)
    # print(bid_list)

    more_bids= str(input('Are there any other bidders? Enter \'Yes\' or \'No\'')).lower()

    if more_bids == 'no':
        os.system('cls')

        for i in range(len(bid_list)):
            if bid_list[i-1]['Amount'] > highest:
               highest = bid_list[i-1]['Amount']
               keep = bid_list[i-1]
            #    keep.append(bid_list[i-1])
        
        # print(keep)
        winner = keep['Name']
        amount = keep['Amount']
        # print(len(bid_list))
        print(f'{winner} have bid highest of ${amount}.')
        bid_status = True
    elif more_bids == 'yes':
        os.system('cls')





