from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.width(1)
tim.speed("fastest")


def random_color():
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    return r, g, b


def draw_circle():
    tim.color(random_color())
    current_heading = tim.heading()
    current_heading += (1)
    tim.setheading(current_heading)
    tim.circle(100)


for n in range(0, 361):
    draw_circle()

screen.exitonclick()
