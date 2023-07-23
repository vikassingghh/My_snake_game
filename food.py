cloor = ["blue", "red", "yellow", "pink", "orange"]
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.colour_snake()
        self.speed("fastest")
        self.refresh()
    
    def colour_snake(self):
        for i in cloor:
            self.color(random.choice(cloor))
        

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
