import turtle
import time
from paddle import Paddle
from ball import Ball
from brick import BrickManager
from scoreboard import Scoreboard

s = turtle.Screen()
s.tracer(0)
s.setup(width=510, height=900)
p = Paddle(0, 430)
sb = Scoreboard()
b = Ball()
bm = BrickManager()
for i in range(bm.row):
    for j in range(bm.heap):
        bm.create_brick(i, j)
s.listen()
s.onkeypress(p.move_left, "Left")
s.onkeypress(p.move_right, "Right")
game_is_on = True

while game_is_on:
    time.sleep(0.03)
    b.move()
    if (b.xcor() > 230) or (b.xcor() < -230):
        b.bounce_x()
    if (b.distance(p) < 50 and b.ycor() > 410) or b.ycor() < -430:
        b.bounce_y()
    if 15 > b.distance(p) >= 0 and b.ycor() > 410:
        b.x = 7 * (b.x//abs(b.x))
        b.y = 13
    if 30 > b.distance(p) >= 15 and b.ycor() > 410:
        b.x = 10 * (b.x//abs(b.x))
        b.y = 10
    if 52 > b.distance(p) >= 30 and b.ycor() > 410:
        b.x = 12 * (b.x//abs(b.x))
        b.y = 8
    # if 50 < b.distance(p) < 10:
    #     b.x = 15
    #     b.y = 5
    if b.ycor() > 430:
        game_is_on = False
    for brick in bm.all_bricks:
        if b.distance(brick) < 30 and b.y > 0:
            brick.hideturtle()
            bm.all_bricks.remove(brick)
            b.bounce_y()
            sb.score += 1
            sb.update_score()
    if not bm.all_bricks:
        game_is_on = False
    s.update()


s.exitonclick()