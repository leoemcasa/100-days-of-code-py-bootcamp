"""Timmy Turtle"""
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# def move_random():
#     """move random"""
#     for _ in range(200):
#         tim.pensize(10)
#         tim.speed(10)
#         tim.color(random_color())
#         tim.setheading(random.choice(angles))
#         tim.forward(20)
#
# move_random()

screen = t.Screen()
screen.exitonclick()
