import turtle
import pandas
from tag import Tag
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

## def get_mouse_click_coor(x, y):
##     print(x, y)
##
## turtle.onscreenclick(get_mouse_click_coor)

is_game_on = True
while is_game_on:
    state_guess = screen.textinput(title="Guess the State", prompt="Write a state's name!").title()
    data = pandas.read_csv("50_states.csv")
    state_ok = data[data.state == state_guess]
    if not state_ok.empty:
        tag = Tag(state_ok)
        scoreboard.increase_score()

# screen.exitonclick()
turtle.mainloop()