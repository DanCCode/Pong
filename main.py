from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddles import Paddles
from ball import Ball
import time

screen = Screen()
turtle = Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.increase_p1_score()
        ball.ball_reset()

    elif ball.xcor() < -380:
        scoreboard.increase_p2_score()
        ball.ball_reset()


screen.exitonclick()
self.x_move *= -1