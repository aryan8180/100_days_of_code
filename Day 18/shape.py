import turtle as t
import random

tim = t.Turtle()

colors = ["Red","Yellow","Green","Blue","Black","Brown","Cyan","Violet","White Smoke","Purple","Gold","Skyblue"]

def draw_share(sides):
    angle = 360 / sides
    for side in range(sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    draw_share(i)