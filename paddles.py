from turtle import Turtle

# CONSTANTS ARE TYPED WITH ALL CAPS
STARTING_POSITIONS = [(-350, 0), (350, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.penup()
        self.turtlesize(5, 1)
        self.color("white")
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
