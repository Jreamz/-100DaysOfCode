from replit import clear
from art import logo

print(logo)

continue_bid = True
bid_dict = {}

def blind_auction(user_name, user_bid):
    bid_dict[name] = bid

def win_bid(record):
    top_bid = 0
    top_name = ""
    for value in bid_dict:
        current_bid = bid_dict[value]
        if current_bid > top_bid:
            top_bid = current_bid
            top_name = value
    print(f"{top_name} has won the auction with a bid of ${top_bid}.")

while continue_bid:
    name = input("What is your name?: ").lower()
    bid = int(input("What's your bid?:  $"))
    continue_bid = input("Would you like to enter another bid? 'Yes' or 'No'\n").lower()
    clear()
    blind_auction(user_name=name, user_bid=bid)
    if continue_bid == "no":
        continue_bid = False
        win_bid(bid)
