from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create()
        self.goto(position)

    def create(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.turtlesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -240:
            self.back(20)
