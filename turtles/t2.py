import turtle

wn = turtle.Screen()

crash = turtle.Turtle()

for z in range(0, 5):
    crash.forward(50)
    crash.right(90)

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

wn.exitonclick()
wn.mainloop()
