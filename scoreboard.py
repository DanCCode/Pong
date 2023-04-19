from turtle import Turtle
from ball import Ball
ALLIGNMENT = "center"

FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        #DRAW SCORE BOARD
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos (0, 260)
        self.write(arg=f"{self.player1_score}   {self.player2_score}", move=False, align=ALLIGNMENT, font=FONT)

    def increase_p1_score(self):
        self.clear()
        self.player1_score += 1
        self.write(arg=f"{self.player1_score}   {self.player2_score}", move=False, align=ALLIGNMENT, font=FONT)

    def increase_p2_score(self):
        self.clear()
        self.player2_score += 1
        self.write(arg=f"{self.player1_score}   {self.player2_score}", move=False, align=ALLIGNMENT, font=FONT)
