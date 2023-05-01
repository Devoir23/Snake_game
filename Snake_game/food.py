from turtle import Turtle
import random

COLOR = ["orange", "red", "blue", "pink", "yellow", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.rand_color = random.choice(COLOR)
        self.color(self.rand_color)
        self.goto(rand_x, rand_y)


