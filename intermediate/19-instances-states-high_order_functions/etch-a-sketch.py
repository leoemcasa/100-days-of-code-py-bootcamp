from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def head_counter_clockwise():
    tim.setheading(tim.heading() + 5)


def head_clockwise():
    tim.setheading(tim.heading() - 5)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=head_counter_clockwise)
screen.onkey(key="d", fun=head_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
