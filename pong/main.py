from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

P1_SCORE = (100, 190)
P2_SCORE = (-100, 190)
P1_POSITION = (350, 0)
P2_POSITION = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

p1_paddle = Paddle(P1_POSITION)
p2_paddle = Paddle(P2_POSITION)
ball = Ball()
score_p1 = Score(P1_SCORE)
score_p2 = Score(P2_SCORE)


screen.listen()
screen.onkey(p1_paddle.move_up, "Up")
screen.onkey(p1_paddle.move_down, "Down")
screen.onkey(p2_paddle.move_up, "w")
screen.onkey(p2_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.current_speed)
    screen.update()
    ball.move()
    if (ball.distance(p1_paddle) < 50 and 340 > ball.xcor() > 330) or \
            ball.distance(p2_paddle) < 50 and -340 < ball.xcor() < -330:
        ball.make_contact()

    if 380 <= ball.xcor():
        score_p2.update_score()

    if ball.xcor() <= -380:
        score_p1.update_score()

    # if score_p1.total_score == 3 or score_p2.total_score == 3:
    #     game_on = False

screen.exitonclick()