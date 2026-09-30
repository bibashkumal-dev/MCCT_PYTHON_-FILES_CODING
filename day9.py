# Nested if conditions:
# username = "shopper"
# password = 123456789

# if username == "shopper":
#     if password == 12345678:
#         print("Login Sucess")
#     else:
#         print("Use Another Password")
# else:
#     print("Login Failed")

#ATM ---> your balance = 10000
#withdarw --> 11000
# balance =int(input("Enter withdraw balance:"))
# if balance >=10000:
#     print("Balance Withdraw Sucessfully")
# else:
#     print("Insufficient Balance")

# saturday and saturday are holidays.
#day = sat or sund ==> holiday
#day = other day (working day)
# nested condition (X)
#use or logic operation

# day = input("Enter the day: ")

# if day == "sat" or day == "sun":
#     print("Holiday")
# else:
#     print("Working Day")

# CHECK THE STRING INSIDE A STRING.
# phrase = "Welcome to Kathmandu"

# if "kathmandu" in phrase:
#     print("Kathmandu  is in phrase")
# else:
#     print("Not Found")

# phrase = "Welcome to Kathmandu"

# if "abc" not in phrase:
#     print("abc is not in phrase")

# sequential algorithmn:
#conditional algorithm:
#IF-ELSE-ELIF.

#ITERATIVE ALGORITHM:
#Loop: A BLOCK CODE EXECUTING REPEATEDLY UNDER A CERTAIN CONDITION OR ACCORDING TO NEED TO ALGORITHM.

# for i in range(100):
#     print("Hello")

# Range:
# 1.range(0,10)
# 0= start , 10= stop point.
# stop point = exclusive(not included)
#ex: 0,1,2,3,4,5,6,7,8,9

# 2. range(10) {stoppie}
#range(1,10)

# 3. range(0,10,2) {0= starting point, 10= stop point and 2= stepup point}
#ex: 0,1,2,3,4,5,6,7,8,9 print zero first and steup with 2 then it print 2 and again stepup then pringt 4 like this upto ....

# range(0,10):
#0,1,2,3,4,5,6,7,8,9,10 (all are i)
#i=0, i=1, i=2

#HELLO
# for i in range(20,4,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)

#COUNT FROM 10 TO 1:
# for i in range(10,1-1):
#     print(i)

#PRINT HELLO TEN TIMES.
# for i in range(0,10):
#     print("Hello")

# for i in range(1,11):
#     print(f"2 x {i}={i*2}")

# for i in range(1, 5):
#     print(i*10)

# CALCULATE THE SUM OF FIRST GIVEN N NUMBER.
num = int(input("Enter a number: "))

sum = 0

for i in range(1,(num+1)):
    sum = sum + i 
    print(f"sum of {num} numbers = {sum} ")