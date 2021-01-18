### JREAMZ VERSION ###

import random
from art import logo

print(logo)
print("Welcome to nebulous numbers, I'm thinking of a number between 1 and 100.")
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ")

difficulty = 0

if user_difficulty == "easy":
    difficulty = 10
elif user_difficulty == "hard":
    difficulty = 5

def random_number():
    num = random.randint(0, 101)
    return num

secret_num = random_number()    

end_game = False

while not end_game:
    if difficulty == 0:
        print("You lose!")
        end_game = True
    for n in range(0, difficulty):
        user_choice = int(input("Make a guess: "))
        
        if user_choice == secret_num:
            print("That's right - you win!")
            end_game = True      
        elif user_choice < secret_num:
            difficulty -= 1
            print("Too low, guess again.")
            print(f"You have {difficulty} attempts remaining to guess the number.")
        else: 
            user_choice > secret_num
            difficulty -= 1
            print("Too high, guess again.")
            print(f"You have {difficulty} attempts remaining to guess the number.")
