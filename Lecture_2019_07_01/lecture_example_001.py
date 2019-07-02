## HEADER DOC BLOCK
# 2019_07_01
import math

def printName(name):
    name = name.capitalize()
    print("Hello", name)


def multiply(x,y):
    #returns a value

    return x * y
    print("this code won't execute")


def circumference(diameter):
    # circumference = diamter * PI
    return diameter * math.pi



## MAIN CODE
def main():
##    name = input("Enter you name:  ")
##    printName(name)
##
##    name = input("Enter you name:  ")
##    printName(name)
##    
    name = input("Enter you name:  ")
    printName(name)
    print(name)
    
    print(multiply(5,10))

    d = 100

    print(circumference(d), "is the circumferece of this circle.  ")

## MAIN CALLOUT
main()
