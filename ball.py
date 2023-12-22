from turtle import Turtle




class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.speed("slow")
        self.penup()
        self.y_step = 10
        self.x_step = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        self.move_speed * 0.6

    def ball_reset_position(self):
        self.goto(0,0)
        self.x_step *= -1
        self.move_speed = 0.1





