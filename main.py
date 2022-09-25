from turtle import Turtle, Screen
import time

screen = Screen()
game_is_on = True
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for pos in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(pos)
    segments.append(new_segment)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x_cor = segments[seg_num - 1].xcor()
        new_y_cor = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x_cor, new_y_cor)
    segments[0].forward(20)

screen.exitonclick()
