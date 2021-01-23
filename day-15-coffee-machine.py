MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


MONEY = 0
PROFIT = 0


def report():
    print(f"Water: {resources['water']}ml ")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g ")
    print(f"Profit: ${PROFIT}")


def user_choice(choice):
    if choice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif choice == "latte":
        resources["water"] -= 200
        resources['milk'] -= 150
        resources["coffee"] -= 24
    elif choice == "cappuccino":
        resources["water"] -= 250
        resources['milk'] -= 150
        resources["coffee"] -= 24


def check_resources(choice):
    global MONEY
    global PROFIT
    if choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18 and MONEY >= 1.5:
            change = MONEY - PROFIT
            PROFIT += 1.5
            print(f"Here is your change: {change}")
            print("Here is your espresso! Enjoy!")
        elif resources["water"] < 50:
            print("Sorry not enough water.")
        elif resources["coffee"] < 18:
            print("Sorry not enough coffee.")
        elif MONEY < 1.5:
            MONEY = 0
            print("Not enough money, you've been refunded.")
    elif choice == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24 and MONEY >= 2.5:
            change = MONEY - PROFIT
            PROFIT += 2.5
            print(f"Here is your change: {change}")
            print("Here is your latte! Enjoy!")
        elif resources["water"] < 200:
            print("Sorry not enough water.")
        elif resources["milk"] < 150:
            print("Sorry not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry not enough coffee.")
        elif MONEY < 2.5:
            MONEY = 0
            print("Sorry not enough money, you've been refunded.")
    elif choice == "cappuccino":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24 and MONEY >= 3.0:
            change = MONEY - PROFIT
            PROFIT += 3.0
            print(f"Here is your change: {change}")
            print("Here is your cappuccino! Enjoy!")
        elif resources["water"] < 200:
            print("Sorry not enough water.")
        elif resources["milk"] < 150:
            print("Sorry not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry not enough coffee.")
        elif MONEY < 3.0:
            MONEY = 0
            print("Sorry not enough money, you've been refunded")
    else:
        print("You did not select an item from the menu.")


def user_money():
    global MONEY
    MONEY = int(input("How many quarters?: ")) * .25
    MONEY += int(input("How many dimes?: ")) * .10
    MONEY += int(input("How many nickels?: ")) * .05
    MONEY += int(input("How many pennies?: ")) * .01
    return MONEY


MACHINE_OFF = False

while not MACHINE_OFF:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        MACHINE_OFF = True
    elif user_input == "report":
        report()
    else:
        user_money()
        if MONEY >= 1.5:
            check_resources(user_input)
            user_choice(user_input)
        elif MONEY >= 2.5:
            check_resources(user_input)
            user_choice(user_input)
        elif MONEY >= 3.0:
            check_resources(user_input)
            user_choice(user_input)
        else:
            print("Not enough money, you've been refunded.")
