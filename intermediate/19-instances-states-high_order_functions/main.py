from turtle import Turtle, Screen
import random

race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "which turtle(color) will win? ")

turtles = []
y = -125
for color in colors:
    turtl = Turtle("turtle")
    turtl.penup()
    turtl.color(color)
    turtl.goto(-230, y)
    y += 50
    turtles.append(turtl)

if user_bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 230:
            race_on = False
            win_color = t.pencolor()
            if user_bet == win_color:
                print(f"You won with {win_color} turtle")
            else:
                print(f"You({user_bet}) lost, {win_color} came first")
        t.forward((random.randint(0,10)))


screen.exitonclick()
