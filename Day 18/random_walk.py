import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")

colors = ["Red","Yellow","Green","Blue","Black","Brown","Cyan","Violet","White Smoke","Purple","Gold","Skyblue"]
direction = [0,90,180,270,650]
tim.pensize(15)

def draw_share(sides):
    for side in range(sides):
        tim.forward(10)
        tim.setheading(random.choice(direction))

for i in range(20):
    tim.color(random.choice(colors))
    draw_share(i)

