from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.rings = []
        self.create_snake()
        self.head = self.rings[0]

    def create_snake(self):
        for ring in STARTING_POSITIONS:
            new_tim = Turtle("square")
            new_tim.color("white")
            new_tim.penup()
            new_tim.goto(ring)
            self.rings.append(new_tim)

    def move(self):
        for ring in range(len(self.rings) -1, 0, -1):
            new_x = self.rings[ring - 1].xcor()
            new_y = self.rings[ring - 1].ycor()
            self.rings[ring].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)