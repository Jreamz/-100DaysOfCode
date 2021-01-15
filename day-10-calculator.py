from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# def operation_choice(choice):
#     if choice == "+":
#         return add(num1, num2)
#     elif choice == "-":
#         return subtract(num1, num2)
#     elif choice == "*":
#         return multiply(num1, num2)
#     elif choice == "/":
#         return divide(num1, num2)

#dictionary operations
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo)

    num1 = float(input("Whats the first number? "))

    for keys in operations:
        print(keys)

    continue_calc = True

    while continue_calc:    
        choice_input= str(input("Pick an operation: "))
        num2 = int(input("Whats the next number? "))
        calculation = operations[choice_input]
        answer = calculation(num1, num2)
        print(f"{num1} {choice_input} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to run again.: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            clear()
            calculator()

calculator()
