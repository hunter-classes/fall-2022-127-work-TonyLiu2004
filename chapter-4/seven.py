import turtle
wn = turtle.Screen()
t1=turtle.Turtle()

for x in (160,-43,270,-97,-43,200,-940,17,-86):
    t1.left(x)
    t1.forward(100)
    
print(t1.heading())