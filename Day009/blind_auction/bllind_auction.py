import os
from art import logo

def adding_bidder():
    print('Welcome to the secret auction program')
    auctioners_name = input('What is your name: ')
    auctioners_bid = int(input('Insert you bid: $'))
    auctioners_dict[auctioners_name] = auctioners_bid
    
def find_winner():
    winner = ''
    bid = 0
    for key in auctioners_dict:
        if auctioners_dict[key] > bid:
            bid = auctioners_dict[key]
            winner = key
    print(f'The winner is {winner} with a bid of ${bid}')
    
auctioners_dict = {}
os.system('clear')
print(logo)
while True:
    adding_bidder()
    more_bidders = input("Are the any other bidder? Type 'yes' or 'no': ")
    if more_bidders == 'yes':
        os.system('clear')
    else:
        os.system('clear')
        find_winner()              
        break


