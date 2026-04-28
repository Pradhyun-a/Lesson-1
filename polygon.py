import turtle

screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(350, 450)

pen = turtle.Turtle()
sides = 6
sideLength = 130
angle = 360 / sides

for i in range(sides):
    pen.forward(sideLength)
    pen.left(angle)
turtle.done()