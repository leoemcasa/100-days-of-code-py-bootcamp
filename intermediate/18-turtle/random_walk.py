"""Timmy Turtle"""
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
angles = [0, 45, 90, 135, 180, 225, 270, 315]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def move_random():
    """move random"""
    for _ in range(200):
        tim.pensize(random.choice([10, 5, 1]))
        tim.speed("fastest")
        tim.color(random_color())
        tim.setheading(random.choice(angles))
        tim.forward(20)

move_random()

screen = t.Screen()
screen.tracer(False)
screen.exitonclick()
