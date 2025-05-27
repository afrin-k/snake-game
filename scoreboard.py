from turtle import Turtle
import os

ALIGN = "center"
FONT = ("Trebuchet MS",20,"bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.f_path = os.path.join(os.path.dirname(__file__),"data.txt")
        with open(self.f_path) as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        
    # score manipulations
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.highscore}",align=ALIGN,font=FONT)

    def increase_score(self):
        self.score += 1 
        self.update_scoreboard()

    # game over message
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.f_path,mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()