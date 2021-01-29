from turtle import Turtle, Screen
import random

tim = Turtle()


screen = Screen()
screen.title("Dot Art")
screen.setup(750, 750)
screen.colormode(255)

color_list = [(229, 225, 221), (218, 229, 220), (233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91),
              (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27),
              (192, 186, 23), (174, 18, 13)]


def random_color():
    return random.choice(color_list)


def draw(x):
    for x in range(x):
        tim.color(random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(50)


tim.penup()

for n in range(0, 451, 50):
    tim.goto(-200, n)
    draw(10)


screen.exitonclick()
