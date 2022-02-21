import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

leonardo.forward(random.randrange(1,101))
michelangelo.forward(random.randrange(1,101))

leonardo.goto(-100,-20)
michelangelo.goto(-100,20)


for number in range(0,10):
  leonardo.forward(random.randrange(0,10))
  michelangelo.forward(random.randrange(0,10)) 

leonardo.goto(-100,-20)
michelangelo.goto(-100,20)

michelangelo.down()
shape_sides=(3,4,6,9,12)
for side in shape_sides:
 angle=360/side
 length=50
for i in range(side):
   michelangelo.down()
   michelangelo.right(angle)
   michelangelo.forward(length)
   michelangelo.up()
michelangelo.clear()

window.exitonclick()
