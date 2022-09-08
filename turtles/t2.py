import turtle

def sample_function():
  print("this is a function")
  print("It can be ran multiple times")

def square(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for z in range(4):
    t.forward(sidelen)
    t.right(90)

  
wn = turtle.Screen()

crash=turtle.Turtle()
square(crash,0,0,3,"blue",50)

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

square(squirt,50,50,3,"red",80)
wn.exitonclick()
wn.mainloop()

sample_function()