import colorgram

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_list = []
# for c in colors:
#     rgb = c.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)
# del rgb_list[:4]
new_rgb_list = [(133, 164, 202), (226, 150, 100), (30, 43, 63), (200, 136, 148), (164, 58, 48), (236, 212, 88), (43, 101, 147), (136, 182, 161), (148, 63, 71), (159, 33, 30), (58, 47, 44), (51, 41, 45), (169, 29, 33), (60, 116, 99), (215, 83, 74), (230, 163, 168), (237, 166, 156), (36, 61, 55), (16, 95, 70), (34, 60, 106), (170, 188, 221), (192, 100, 108), (104, 127, 161), (19, 84, 104), (174, 200, 189), (36, 150, 208)]

import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

t.penup()
t.setheading(225)
t.forward(350)
t.setheading(0)

for cycle in range(10):
    for dot in range(10):
        t.dot(20, random.choice(new_rgb_list))
        t.penup()
        t.forward(50)
        t.pendown()

    t.penup()
    t.back(500)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.pendown()

screen = turtle.Screen()
screen.exitonclick()
