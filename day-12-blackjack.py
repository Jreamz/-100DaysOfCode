from replit import clear
from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def draw_card():
    """"return a random card from cards list"""""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Take a list of cards and return the score calculated via sum"""
    sum_cards = sum(cards)
    if sum_cards == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum_cards > 21:
        cards.remove(11)
        cards.append(1)
        return sum_cards
    else:
        return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
       return "Draw!"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack!"
    elif user_score == 0:
        return "You win! Blackjack!"
    elif user_score > 21:
        return "Bust - You lose!"
    elif computer_score > 21:
        return "You win! Opponent busts."
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You lose!"

def black_jack():
    user_cards = []
    computer_cards = []
    game_over = False

    print(logo)

    for n in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_again = input("Do you want to draw another card? 'y' to draw, 'n' to pass: ")

        if draw_again == "y":
            user_cards.append(draw_card())
        else:
            game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input(f"Would you like to play Blackjack? 'y' or 'n': ") == "y":
    clear()
    black_jack()
