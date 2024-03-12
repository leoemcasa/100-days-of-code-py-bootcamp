import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## def get_mouse_click_coor(x, y):
##     print(x, y)
##
## turtle.onscreenclick(get_mouse_click_coor)

states_guessed = []
while len(states_guessed) < 50:
    state_guess = screen.textinput(title=f"{len(states_guessed)}/50 StateS Correct. (X) to Exit", prompt="Write a state's name!").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if state_guess == "X":
        states_missing = [e for e in all_states if e not in states_guessed]
        new_data = pandas.DataFrame(states_missing)
        new_data.to_csv("states_to_learn.csv")
        break
    if state_guess in all_states:
        states_guessed.append(state_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_ok = data[data.state == state_guess]
        t.goto(int(state_ok.x), int(state_ok.y))
        t.write(state_guess)
        print(state_ok.state.item())

# screen.exitonclick()
turtle.mainloop()
