from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Tag(Turtle):
    def __init__(self, state_ok):
        super().__init__()
        self.state_series = state_ok.squeeze()
        self.state_list = self.state_series.tolist()
        self.state = self.state_list[0]
        self.state_x = int(self.state_list[1])
        self.state_y = int(self.state_list[2])
        self.penup()
        self.hideturtle()
        self.goto(self.state_x, self.state_y)
        self.write(self.state, align=ALIGNMENT, font=FONT)
