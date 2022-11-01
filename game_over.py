from turtle import Turtle

class Game_over(Turtle):
    def __init__(self):
        super().__init__()

        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER BITCH", align= "center", font=( "Courier", 24, "normal") )

