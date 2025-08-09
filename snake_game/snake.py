from turtle import Turtle

COLOR = "white"
SHAPE = "square"
MOVE_DISTANCE = 20
X_START_COR = 0
Y_START_COR = 0
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self, num_segs):
        self.snake = []
        self.initial(num_segs)
        self.head = self.snake[0]

    def initial(self,segs):
        for num in range(0, segs):
            self.add_seg((X_START_COR + (num * -20), Y_START_COR))
            self.snake[num].teleport(x=X_START_COR + (num * -20), y=Y_START_COR)


    def movement(self):
        for section in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[section - 1].xcor()
            new_y = self.snake[section - 1].ycor()
            self.snake[section].teleport(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    def add_seg(self, position):
        segment = Turtle(shape=SHAPE)
        segment.color(COLOR)
        segment.penup()
        segment.shapesize(1, 1)
        segment.speed('slowest')
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.add_seg(self.snake[-1].position())

    def snake_reset(self):
        for seg in self.snake:
            seg.goto(1000, 1001)
        self.snake.clear()
        self.initial(3)
        self.head = self.snake[0]