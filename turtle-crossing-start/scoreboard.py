FONT = ("Courier" , 24 , "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__( self ):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(0 , 270)
        self.update_score_board()

    def update_score_board( self ):
        self.clear()
        self.write(f"Level: {self.score}" , align="center" , font=FONT)

    def increase_score( self ):
        self.score += 1
        self.update_score_board()

    def game_over( self ):
        self.goto(x=0 , y=0)
        self.write(f"Game Over! Your Score:{self.score}" , align="center" , font=FONT)
