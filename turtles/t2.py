import turtle

def sample_function():
  print("this is a function")
  print("It can be ran multiple times")

def square(t):

  for z in range(0, 5):
    t.forward(50)
    t.right(90)

  
wn = turtle.Screen()

crash=turtle.Turtle()
square(crash)

squirt = turtle.Turtle()
squirt.color("red")
squirt.width(5)
squirt.penup()
squirt.left(180)
squirt.forward(50)
squirt.left(90)
squirt.forward(50)
squirt.right(90)
squirt.pendown()
for x in range(0, 4):
    squirt.forward(50)
    squirt.right(120)

square(squirt)
wn.exitonclick()
wn.mainloop()

sample_function()