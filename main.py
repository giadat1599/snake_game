from turtle import Turtle, Screen
from snake import Snake
import time

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
