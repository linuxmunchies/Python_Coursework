################################################################################
# LAB2
################################################################################

import math      # you may need the math module to answer some of the questions

################################################################################

def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; 
    return 'Redacted ForPrivacy'


def bmiCalculator(wt,h):
    return (wt * 703) / h**2 #ADD CODE HERE
    

def f(x,y):
    return int(math.floor(((x + y)**3) / (math.sqrt(x**2 + y**2)))) #ADD CODE HERE


def averageOfThree (f1, f2, f3):
    return (f1 + f2 + f3) / 3 #ADD CODE HERE


def nMultiplier (n):
    return n + n*11 + n*111 #ADD CODE HERE


def fahr2celsius (f):
    return (f - 32) * (5 / 9) #ADD CODE HERE

def volumeSphere (r):
    return (4/3) * math.pi * r**3 #ADD CODE HERE



########################################################
# Function Calls
########################################################
print ("\n**************************************\n")
print("My name is : {}".format(myName()))

print ("\n**************************************")
wt=250
h=72
print ("The result of BMI calculation")
print(bmiCalculator(wt,h))
print ("\n**************************************")

x=3
y=4
print ("The result of f function ")
print(f(x,y))
print ("\n**************************************\n")



f1=10.2
f2=20.3
f3=30.1
print ("The result of averageOfThree function ")
print(averageOfThree (f1, f2, f3))
print ("\n**************************************\n\n")


n=5
print ("The result of nMultiplier function ")
print(nMultiplier (n))
print ("\n**************************************\n\n")


f=74
print ("The result of Fahrenheit to Celsius calculation")
print(fahr2celsius (f))
print ("\n**************************************\n\n")


r=10
print ("The result of volumeSphere ")
print(volumeSphere (r))
print ("\n**************************************\n\n")
