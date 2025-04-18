from turtle import Turtle
import random

class Food( Turtle):
   
    def __init__(self):     
        super().__init__()
        self.shape("circle")
        self.penup()    
        self.shapesize(stretch_len = 0.8, stretch_wid= 0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280,290) 
        random_y = random.randint(-280,200)      
        self.goto(random_x,random_y)
        