from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center",font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=('Arial', 20, 'normal'))

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")