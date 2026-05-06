from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"



class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.ht()
    self.speed(0)
    self.penup()
    self.shape("square")
    self.st()
    self.alive = True
    screen.onkeypress(self.left, "Left")
    screen.onkeypress(self.right, "Right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")

  def up(self):
    if self.heading()!=-90:
      self.setheading(90)
    

  def down(self):
    if self.heading() != 90:
      self.setheading(-90)
    


  def left(self):
    if self.heading() != 0:
      self.setheading(180)


  def right(self):
    if self.heading() != 180:
     self.setheading(0)


  def move(self):
    self.forward(20)
    if self.xcor() > 230 or self.xcor() < -230:
        self.die()
    if self.ycor() > 230 or self.ycor() < -230:
        self.die()

  def die(self):
    self.ht()


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.speed(0)
    self.shape("square")
    self.goto(other.xcor(),other.ycor())
    self.st()

  def move(self, other):
    self.goto(other.xcor(),other.ycor())
    



class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.goto(random.randint(-200,200), random.randint(-200,200))
    self.showturtle()

  def relocate(self):
    self.goto(random.randint(-200,200), random.randint(-200,200))



def update ():
  if player.alive:
      player.move()
      for i in range(len(body)-1,0,-1): 
        body[i].move(body[i-1])
      if player.distance(apl)<20:
        apl.relocate()
        body.append(Segment(body[-1]))
    

      for i in range(len(body)):
          if player.distance(body[i]) > 20:
            player.color("red")
  screen.ontimer(update,10)




screen = Screen()
screen.bgcolor("lightblue")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
screen.onkey(update,"space")




player = Head(screen)
apl = Apple() 
body = [player]

screen.exitonclick()
