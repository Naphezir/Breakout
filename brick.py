import turtle


class BrickManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_bricks = []
        self.initial_x = -212
        self.initial_y = -427
        self.row = 7
        self.heap = 4
        self.x = 70
        self.y = 30

    def create_brick(self, x, y):
        brick = turtle.Turtle()
        brick.penup()
        brick.shape("square")
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.goto(self.initial_x + (self.x * x), self.initial_y + (self.y * y))
        self.all_bricks.append(brick)

    def destroy_brick(self):
        del self
