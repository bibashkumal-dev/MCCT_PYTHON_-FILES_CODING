# Euclid's Algorithm to find GCD

a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("The GCD is:", a)


while b != 0: