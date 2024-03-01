import random
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


# tim.shape("turtle")
# tim.color("coral")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = (r, g, b)
    return c


def square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


# square()

def dashed_line():
    for _ in range(15):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


# dashed_line()
# colors = ["light sky blue", "spring green", "hot pink", "medium purple", "yellow", "orange red", "red", "lawn green",
#           "medium blue"]

directions = [0, 90, 180, 270]


def shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


# for shape_sides_number in range(3, 11):
#     tim.color(random.choice(colors))
#     shape(shape_sides_number)

# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     # tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# draw_spirograph(5)

screen = Screen()
screen.exitonclick()

# playing with github
