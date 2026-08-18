import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for i in range(240):
    t.pencolor(colors[i % 6])
    t.circle(i, 90)
    t.forward(i)
    t.left(89)
turtle.done()
