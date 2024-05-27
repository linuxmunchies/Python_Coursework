#Lab10

import random as rand

def sumOfN(n):
    """
    sumOfN: takes in integer n and finds 1 + .. + n
    n: integer
    sumOfN(5)
    Expected Output: 15
    """

    if n <= 1:
        return n
    else:
        return n + sumOfN(n-1)

#print("The output of sumOfN: ")
#print(sumOfN(5))

def factorial(f):
    """
    factorial: calculates f! for integer f
    f: integer
    factorial(6)
    Expected Output: 720
    """

    if f<= 1:
        return f
    
    return f * factorial(f-1)

#print("The output of factorial: ")
#print(factorial(6))

def fibonacci(n):
    """
    fibonacci: calculates the nth number of the fibonacci sequence 
    n: integer
    fobonnaci(10)
    Expected Output: 34
"""

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print("The expected output of fibonacci: ")
#print(fibonacci(10))

""" Takes integer n and finds the sum
    of all the values between 1 and n, including n.
    Expected Output: 30
"""
def sumOfEven(n):
    if n <= 1:
        return 0
    elif n % 2 == 1:
        return sumOfEven(n-1)
    elif n % 2 == 0:
        return n + sumOfEven(n-1)
    else:
        print("UH oh error! :(")

#print(sumOfEven(10))

""" gNumGame()
Takes no inputs. It is basically a number guessing game.
Tells the user if they are too high or too low.
Number should be between 1 and 100, including them both.
"""
def gNumGame():
    genNum = rand.randint(1, 101)
    print("Please input your guess! Between 1 and 100, including them!")
    userNum = int(input("\n: "))
    winStatus = 0
    userGuesses = 0
    while winStatus == 0:
        if userNum == genNum:
            print("Congratulations! You won!")
            winStatus = 1
        elif userNum > genNum:
            print("Your number is too high. Try again!")
            userNum = int(input("\n:"))
            userGuesses += 1
        elif userNum < genNum:
            print("Your number is too low. Try again!")
            userNum = int(input("\n:"))
            userGuesses += 1
        else:
            print("Something has gone wrong.")
    print(f"You guessed in {userGuesses} guesses!")
gNumGame()