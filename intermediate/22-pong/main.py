from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_POSITION = 350

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(PADDLE_POSITION)
l_paddle = Paddle(PADDLE_POSITION * -1)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall hit
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect paddle hit
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # R paddle misses
    if ball.xcor() > 380:
        ball.rset_position()
        scoreboard.l_point()

    # R paddle misses
    if ball.xcor() < -380:
        ball.rset_position()
        scoreboard.r_point()



screen.exitonclick()
