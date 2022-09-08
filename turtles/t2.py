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

def triangle(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(3):
    t.forward(sidelen)
    t.left(120)


def ngon(t,x,y,w,color,sidelen,sides):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(sides):
    t.forward(sidelen)
    t.right(360/sides)
  
wn = turtle.Screen()

crash=turtle.Turtle()
square(crash,0,0,3,"blue",50)

squirt=turtle.Turtle()
square(squirt,50,50,3,"red",80)

tri=turtle.Turtle()
triangle(tri,-50,-50,3,"yellow",50)

gon=turtle.Turtle()
ngon(gon,0,50,3,"green",50,8)

wn.exitonclick()
wn.mainloop()

sample_function()