"""Timmy Turtle"""
import turtle as t
import random

tim = t.Turtle()
colours = ["red", "blue", "black", "orange", "green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_num_sides in range (3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_num_sides)

screen = t.Screen()
screen.exitonclick()
