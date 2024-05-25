import turtle
import random as rand
screen = turtle.Screen()
lilT = turtle.Turtle()

def myName():
    return "Redacted ForPrivacy"

# turtleDrawSquare draws a square of length n
def turtleDrawSquare(n):
    for x in range(4):
        lilT.forward(n)
        lilT.left(90)

# turtleDrawSquare draws a circle with diameter n
def turtleDrawCircle(n):
    lilT.circle(n)

# turtleDrawSquare draws a rectangle with length n * 2 and width n
def turtleDrawRectangle(n):
    lilT.forward(2*n)
    lilT.left(90)
    lilT.forward(n)
    lilT.left(90)
    lilT.forward(2*n)
    lilT.left(90)
    lilT.forward(n)
    lilT.left(90)

# turtleDrawTriangle draws a triangle with sides length n
def turtleDrawTriangle(n):
    lilT.forward(n)
    lilT.left(120)
    lilT.forward(n)
    lilT.left(120)
    lilT.forward(n)
    lilT.left(120)

# turtleDrawPentagon draws a pentagon where every side is n
def turtleDrawPentagon(n):
    lilT.forward(n)
    lilT.left(72)
    lilT.forward(n)
    lilT.left(72)
    lilT.forward(n)
    lilT.left(72)
    lilT.forward(n)
    lilT.left(72)
    lilT.forward(n)
    lilT.left(72)

# NumGeneratorHW5 is a program I made to generate all the required numbers
    # for the actual randomness factors required by HW5's Problem
def numGeneratorHW5():
    shapeNum = rand.randint(0, 4)
    RGBR = rand.randint(0, 255)
    RGBG = rand.randint(0, 255)
    RGBB = rand.randint(0, 255)
    pixelNum = rand.randint(51, 149)
    xCord = rand.randint(0,250)
    yCord = rand.randint(0,250)
    return [shapeNum, RGBR, RGBG, RGBB, pixelNum, xCord, yCord]

# START OF CODE -- INITIALIZATION COMPLETE
# Runs the following functions to setup our turtle
randList = numGeneratorHW5()
lilT.up()
screen.colormode(255)
lilT.pencolor(randList[1],randList[2],randList[3])
lilT.goto(randList[5], randList[6])
lilT.down()

# Send all generated values and colors to appropriate drawing tool.
if randList[0] == 0:
    turtleDrawSquare(randList[4])
if randList[0] == 1:
    turtleDrawCircle(randList[4])
if randList[0] == 2:
    turtleDrawRectangle(randList[4])
if randList[0] == 3:
    turtleDrawTriangle(randList[4])
if randList[0] == 4:
    turtleDrawPentagon(randList[4])


screen.exitonclick()