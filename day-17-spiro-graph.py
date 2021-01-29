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


def draw_circle(gap):
    for n in range(int(360 / gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + gap)
        tim.circle(100)


draw_circle(10)

screen.exitonclick()
