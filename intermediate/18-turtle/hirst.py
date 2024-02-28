# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
#
# rgb_colors = []
# for e in colors:
#     r = e.rgb.r
#     g = e.rgb.g
#     b = e.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_mod
import random

color_list = [(236, 35, 108), (145, 28, 66), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35), (239, 162, 194), (147, 26, 24), (242, 168, 158), (162, 211, 178), (140, 211, 232), (7, 115, 55), (26, 186, 225), (84, 133, 177), (163, 193, 227), (112, 9, 8)]
turtle_mod.colormode(255)
tim = turtle_mod.Turtle()

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_mod.Screen()
screen.exitonclick()
