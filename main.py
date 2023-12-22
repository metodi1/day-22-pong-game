from turtle import Turtle, Screen

from ball import Ball
from pad import Paddle
from scorebord import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)
screen.listen()

left_paddle = Paddle(-380, 0)
right_paddle = Paddle(380, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision wiht the wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision wiht the paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 349 or ball.distance(left_paddle) < 40 and ball.xcor() < -349:
        ball.bounce_x()

    # ball reset
    if ball.xcor() > 390:
        ball.ball_reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.ball_reset_position()
        scoreboard.r_point()

    screen.update()

screen.exitonclick()
