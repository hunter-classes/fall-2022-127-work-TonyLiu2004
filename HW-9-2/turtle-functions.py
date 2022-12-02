import turtle

def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(6):
    t.forward(sidelen)
    t.right(60)


def ngon(t,x,y,w,color,sidelen,sides):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(sides):
    t.forward(sidelen)
    t.right(360/sides)

wn=turtle.Screen()
cookie=turtle.Turtle()
hexagon(cookie,50,0,3,"green",50)

biscuit=turtle.Turtle()
ngon(biscuit,-100,0,3,"red",50,10)

wn.exitonclick()
wn.mainloop()