from turtle import Turtle, Screen
import random

colors = ["Blue", "Orange", "Pink", "Green", "Red", "Purple"]
y_pos = [-75, -50, -25, 25, 50, 75]

screen = Screen()
screen.title("Turtle 500")
screen.setup(width=500, height=500)

race = False
user_bet = screen.textinput(title="Place your bet:", prompt="Who will win the race?")

turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_pos[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    race = True

while race:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win the bet! The winner is {winner}")
            else:
                print(f"You've lost - The winner is {winner}!")

        random_num = random.randint(0, 10)
        turtle.forward(random_num)

screen.exitonclick()
