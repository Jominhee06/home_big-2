import turtle
import random


def screenLeftclick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screenRightclick(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screenMidclick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)

    r = random.random()
    g = random.random()
    b = random.random()

    pSize = 10
    r, g, b = 0.0, 0.0, 0.0

    turtle.title('거북이로 그림 그리기')
    turtle.shape('turtle')
    turtle.pensize(pSize)

    turtle.onscreenclick(screenLeftclick, 1)
    turtle.onscreenclick(screenMidclick, 2)
    turtle.onscreenclick(screenRightclick, 3)


# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)

turtle.done()