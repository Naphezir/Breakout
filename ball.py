import turtle
import random

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.x = random.choice([-12, -10, -7, 7, 10, 12])
        self.y = random.choice([-12, -10, -7, 7, 10, 12])

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() - self.y)

    def bounce_x(self):
        self.x *= -1

    def bounce_y(self):
        self.y *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def update_x(self, new_x):
        self.x = new_x

    def update_y(self, new_y):
        self.y = new_y
