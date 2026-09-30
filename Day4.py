# # Escape character
# \n --> line break
# \t --> TAB

#Output:
#Name   Ram
#Age    18

print("Name\tRam\nAge\t18")
#Output
#Amount = Rs.150,000
Amount = 150000
print(f"Amount = Rs.{Amount:,}")

#Decimal Formatting
x = 58.1234567890
print(f"{x:.2f}")

y = 23.56789876543345
print(f"{y:.2f}")

#scaling 
#Name   Age
#Shyam  18
#Ram    19
#Sita   18
print(f"{'Name':<10}{'Age':<5}")
print(f"{'Ram':<10}{'19':<5}")
print(f"{'Shyam':<10}{'18':<5}")
print(f"{'Sita':<10}{'18':<5}")

#ASCII Characters
#American Standard Code for Information Interchange
# How to convert the ASCII to Character and Vice-Versa.
x = "A"
print(f"{ord(x)}")
y = 67
print(f"{chr(y)}")

#Mathematical Operations:
#Adddition
#Subtraction
#Multiplication
#Division
#floor Division
#Modulus
#Percentge

#Take a input of two number from user and perform all above
#operations.

#Taking user input.
#Enter your Name:

#var1 = input("Enter your Name:")
#print(type(var1))

#var1 = float(input("Enter First Number:"))
#var2 = float(input("Enter Second Number:"))

#print(f"sum = {var1+var2}")
#Addition
#print(f"Addition=", var1+var2)

#Subtraction
#print(f"Subtraction:", var1-var2)

#Multiplication
#print(f"Mulriplication:", var1*var2)

#Division
#print(f"Division:", var1 / var2)

#floor division
#print(f"floor division:", var1 // var2)

#Modules
#print(f"Modules:", var1 % var2)

#percentage
#print(f"percentage:", (var1 / var2) * 100)


# Taking user input
#var1 = float(input("Enter First Number:"))
#var2 = float(input("Enter Second Number:"))

#print(f"Sum = {var1+var2}\nDifference = {var1-var2}\nProduct = {var1*var2}")
#print(f"Percentage = {(var1/var2)*100:.2f}%")

num1 = 25
if num1 % 2 ==0:
    print("Even")
else: 
    print("Odd")
###################
num1 = 25
if num1 % 2 == 1:
    print("Odd")
else:
    print("Even")

print(58 ** 25)

10 + (5 x 2) = 20



import math

print(math.sqrt(250))
print(math.pow(2,10))

num1 = 10.51234
print(round(num1))