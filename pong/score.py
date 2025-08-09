from turtle import Turtle

FONT =("Arial", 100, "bold")

class Score(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.total_score = 0
        self.goto(coordinates)
        self.write(f"{self.total_score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.total_score += 1
        self.write(f"{self.total_score}", align="center", font=FONT)
