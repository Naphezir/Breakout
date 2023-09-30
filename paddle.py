import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(x, y)

    def move_left(self):
        self.goto(self.xcor()-20, self.ycor())

    def move_right(self):
        self.goto(self.xcor()+20, self.ycor())