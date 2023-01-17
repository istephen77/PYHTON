from turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(120):
    color('purple')
    circle(i)
    color('purple')
    circle(i*0.8)
    right(3)
    forward(3)
done()