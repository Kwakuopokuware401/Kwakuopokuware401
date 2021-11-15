import turtle
t = turtle.Pen()
turtle.bgcolor("black") #adding background colour
colors = ["red", "yellow", "blue", "green"] #list of colours used
for x in range(100):
 t.pencolor(colors[x%4])
 t.circle(x)
 t.left(91)
