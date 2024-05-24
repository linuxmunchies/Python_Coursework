################################################################################
# HW1
################################################################################

import math      # you will need the math module to answer some of the questions

################################################################################

def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Redacted ForPrivacy'



######################################################################
# HW1 PROBLEMS
######################################################################

# check hw1.pdf file to see implemented test cases and expected outputs
def f(x): 
    return 5*x - 3

def areaOfTriangle (h, b):
    
    return (1/2) * b * h


def phoneBill (m,tx):
    return (15 + 0.44 + ((m-50) * 0.25) + ((tx - 50) * 0.15)) + 0.05 * (15 + 0.44 + ((m-50) * 0.25) + ((tx - 50) * 0.15))# ADD CODE HERE


def grader (avg_exams, avg_hw, attendance):
    if (attendance > 18 and avg_exams > 75 and avg_hw > 75) and (avg_exams > 80 or avg_hw > 80):
        return(1)
    else:
        return(0) 


def radToDegree(rad):
    return rad * (180/math.pi)



def sizeOfLine (x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)





########################################################
# Function Calls
# Do not Change/modify/touch.. any code below
########################################################
print ("\n**************************************\n\n")
print("My name is : {}".format(myName()))

print ("\n\n**************************************")
x=5
print ("The result of practice problem f(x)")
print(f(x))
print ("\n**************************************")

h=3
b=15.2
print ("The result of areaOfTriangle (h, b)")
print(areaOfTriangle (h, b))
print ("\n**************************************")


m=70
tx=120
print ("The result of phoneBill (m,tx)")
print(phoneBill (m,tx))
print ("\n**************************************")


avg_exams = 72
avg_hw = 88
attendance =22
print ("The result of grader (avg_exams, avg_hw, attendance) ")
print(grader(avg_exams, avg_hw, attendance))
print ("\n**************************************")


rad=100
print ("The result of radToDegree(rad) ")
print(radToDegree(rad))
print ("\n**************************************")



x1=200
y1=200
z1=200
x2=203
y2=204
z2=200
print ("The result of sizeOfLine (x1, y1, z1, x2, y2, z2)")
print(sizeOfLine (x1, y1, z1, x2, y2, z2))
print ("\n**************************************")



