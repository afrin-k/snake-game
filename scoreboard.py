from turtle import Turtle
ALIGN = "center"
FONT = ("Trebuchet MS",20,"bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    # score manipulations
    def update_scoreboard(self):
        self.write(f"Score = {self.score}",align=ALIGN,font=FONT)

    def increase_score(self):
        self.score += 1 
        self.clear()
        self.update_scoreboard()

    # game over message
    def game_over(self):
        self.clear()
        self.write(f"Game Over.",align=ALIGN,font=FONT)
        self.goto(0,0)