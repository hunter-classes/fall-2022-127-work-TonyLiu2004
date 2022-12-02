import turtle
screen=turtle.Screen()
t1=turtle.Turtle()

for x in range(0,15,1):
  t1.forward(30)
  t1.right(30)

screen.exitonclick()
screen.mainloop()