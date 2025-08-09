from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

new_time = time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(num_segs=3)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True
while game_is_on:
    new_time.sleep(0.1)
    screen.update()
    snake.movement()

    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
        snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.score_reset()
        snake.snake_reset()


    for segment in snake.snake[1:]:
        if snake.head.distance(segment.position()) < 10:
            scoreboard.score_reset()
            snake.snake_reset()


screen.exitonclick()
