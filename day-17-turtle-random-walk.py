from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen_x = 900
screen_y = 900
screen.setup(screen_x, screen_y)

tim = Turtle()
tim.shape("turtle")
tim.width(4)
tim.speed(2)

direction = [0, 90, 180, 270]


def random_color():
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)

    return r, g, b



def random_walk():
    tim.color(random_color())
    tim.seth(random.choice(direction))
    tim.forward(random.randint(0, 42))


keep_walking = True

while keep_walking:
    random_walk()


screen.exitonclick()
