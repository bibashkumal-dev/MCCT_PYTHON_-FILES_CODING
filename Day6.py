#1. Some useful Functions:

#1. print()
#2. Sum()
#num1 = 50
#num2 = 20

#print(f"sum = {sum([num1 + num2])}")

#3 Round()
#Num3 = 10.11234
#print(round(Num3))

#4 Asolute Value()-->
#print(abs(-25))

#import math
#r = 10
#area_circle = math.pi * r ** 2
#print(area_circle)

#import math
#d = 28
#area_circle = math.pi * d/2 **2
#print(f"Area = {math.pi*(d/2)**2:.2f}")


#num1 = float(input("Enter first number:"))
#num2 = float(input("Enter second number:"))

#sum = num1 + num2
#print(f"Sum = {sum([num1, num2])}")

#print(f"Minimum = {min(num1, num2)}")
#print(f"Maximunm = {max(num1, num2)}")

#print(f"Power = {math.pow(num1,2)}")

#5 Functions:
def abc(name): # name = parameter
    print("Hello", name)
abc("World") # world = arguument
abc("RAM")
abc("SHYAM")


# Def means "defining the function name"
#func = name of a function.
# () ==> All the parameters will be here
# : ===> end of function decelration and start of function of body.


# Indentation:
# The spaces given after the condition statement, function/ class, decleration and loop statement.


# Addition:
def add(a,b):
    print(a+b)
add(10,20)

bus = 500
food = 1500
#calculate the monthly expense in bus + food.

def add(bus,food):
    print(bus+food)
add(500,1500)

def add(gym,diet,clothes,travelling):
    print(gym+diet+clothes+travelling)
add(2000,3500,1500,2000)

# Subtraction:
def sub(gym,diet,travelling):
    print(gym-diet-travelling)
sub(2000,1500,800)

def sub(food,casino):
    print(food-casino)
sub(5000,3000)

# Multiplication:
def mul(food,bus):
    print(food*bus)
mul(500,800)

#Division:
def div(bus, food):
    print(bus/food)
div(5000,2500)

# return vs print:
def add(a,b):
    return(a + b)
result = add(10,20)
print(result)

#print= doesnt store value just show in terminal as a output by printing .
#return= store the value and show as a result in output to.

#fruitful and not-fruitful.












