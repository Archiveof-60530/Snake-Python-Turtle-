from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()



class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()

  def up(self):
    self.setheading(90)
    self.sety(self.ycor()+10)

  def down(self):
    self.setheading(-90)
    self.sety(self.ycor()-10)


  def left(self):
    self.setheading(180)
    self.setx(self.xcor()-10)


  def right(self):


  def move(self):

    
  def die(self):




class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass



class Apple(Turtle):
  def __init__(self):
    super().__init__()
    pass

  def relocate(self):
    pass


screen = Screen()
screen.bgcolor("lightblue")
screen.setup(520,520)
screen.listen





screen.exitonclick()