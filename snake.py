from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_num - 1].xcor()
            new_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cor, new_y_cor)
        self.segments[0].forward(MOVE_DISTANCE)
