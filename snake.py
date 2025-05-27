from turtle import Turtle
POSITIONS = [(-20,0),(0,0),(20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # creating and extending the snake
    def create_snake(self):
        for p in POSITIONS:
            self.add_segment(p)

    def add_segment(self,position):
        body_segment = Turtle("square")
        if position == (-20,0):
            body_segment.color("lightslategrey")
        else:
            body_segment.color("white")
        body_segment.penup()
        body_segment.goto(position)
        self.segments.append(body_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    # moving the snake
    def move(self):
        segments = self.segments
        for snum in range(len(segments)-1,0,-1):
            new_x = segments[snum-1].xcor()
            new_y = segments[snum-1].ycor()
            segments[snum].goto(new_x,new_y)
        segments[0].forward(MOVE_DISTANCE)
    
    # changing directions of the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]