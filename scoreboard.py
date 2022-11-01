from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 250)
        self.write( self.score,  align= "center" ,font =  FONT)
        self.goto(-210,250)
        self.write("Level: ", align= "center", font = FONT)
    def add_point(self):
        self.score += 1
        self.update_score()

