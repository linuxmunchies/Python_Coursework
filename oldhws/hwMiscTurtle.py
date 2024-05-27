import turtle
import random

screen = turtle.Screen()
lilT = turtle.Turtle()

def turtleDrawLine(len):
    lilT.forward(len)

def turtleDrawLineRandom(len, lineW):
    ranNum = random.randint(5, 25)
    lilT.pensize(lineW)
    for x in range(ranNum):
        lilT.forward(len)
        lilT.setheading(random.randint(0, 360))

def turtleDrawSquare(len):
    for x in range(4):
        lilT.forward(len)
        lilT.left(90)

def triangleChecker(f1, f2, f3):
    if ((f1 + f2) > f3 or (f2 + f3) > f1 or (f3 + f1) > f2):
        if f1 == f2 == f3:
            print("The triangle is valid. It is an equilateral triangle.")
        elif (f1 != f2 and f2 != f3 and f3 != f1):
            print("The triangle is valid. It is a scalene triangle.")
        elif (f1 == f2 or f2 == f3 or f3 == f1):
            print("The triangle is valid. It is an isosceles triangle.")
        else:
            print("Something's gone wrong!")
    else:
        print("The triangle provided is not valid.")

def turtleDrawRandTriangle():
    for _ in range(3):
        lilT.forward(random.randint(50, 100))
        lilT.left(random.randint(0, 120))

turtleDrawRandTriangle()

screen.exitonclick()
