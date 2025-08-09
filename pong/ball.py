from turtle import Turtle
import random

SIDE_NAME = ("left", "right")

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_direction(random.choice(SIDE_NAME))
        self.current_speed = .1

    def set_direction(self, side):
        if self.xcor() == 0 and self.ycor() == 0:
            if side == "right":
                new_heading = random.randint(-80, 80)
            elif side == "left":
                new_heading = random.randint(110, 260)
            else: new_heading = 360 - self.heading()
        else:
            new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def make_contact(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
        self.forward(20)
        self.current_speed /= 1.3

    def reset_position(self):
        self.goto(0,0)
        self.current_speed = .1

    def move(self):
        if 380 < self.xcor():
            self.reset_position()
            self.set_direction("left")
            self.forward(20)
        elif self.xcor() < -380:
            self.reset_position()
            self.set_direction("right")
            self.forward(20)
        elif self.ycor() > 280 or self.ycor() < -280:
            self.set_direction("NONE")
            self.forward(20)
        else:
            self.forward(20)
