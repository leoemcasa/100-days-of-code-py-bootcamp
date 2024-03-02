from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.add_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("!!! GAME OVER !!!", align=ALIGN, font=FONT)
