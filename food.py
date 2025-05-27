from turtle import Turtle
import random
COLORS = ["lightpink","lightskyblue","yellow","green","orange"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white","green")
        self.speed("fastest")
        random_x = random.randint(-260,260)
        random_y = random.randint(-260,260)
        self.goto(random_x,random_y) 

    # placing food at different locations
    def refresh(self):
        self.color("white",random.choice(COLORS))
        random_x = random.randint(-260,260)
        random_y = random.randint(-260,260)
        self.goto(random_x,random_y) 