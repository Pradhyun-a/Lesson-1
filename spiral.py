import turtle

screen = turtle.Screen()
screen.bgcolor("blue")

pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        pen.forward(size + 10)
        pen.left(90)
    size = size + 5