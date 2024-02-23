"""Turtle Graphics"""
import turtle
from turtle import Turtle, Screen

tommy = turtle.Turtle()
timmy = Turtle()
tommy.shape("turtle")
tommy.color("aquamarine3", "coral")
tommy.shapesize(3, 3, 2)
timmy.shape("turtle")
timmy.color("green", "aquamarine3")
timmy.shapesize(3, 3, 2)
timmy.speed("slowest")
timmy.fd(100)

my_screen = Screen()
my_screen.exitonclick()
