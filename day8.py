# CONDITIONAL STATEMENT AND CONDITIONAL OPERATORS.
# vali_id = True
# if vali_id:
#     print("You are a active student")

#a=23
#if a> 18:
    #print("you are elder than 18.")
#else:
    #print("you are younger")

#age = int(input("Enter your age "))
#if age >= 18:
    #print("Apply for Drivers license")
#else: 
    #print("Cannot Apply for Drivers license")
# obtained_marks = float(input("Enter marks:"))
# if obtained_marks>=40:
#     print("You are pass")
# else:
#     print("You are fail")

#if - else conditions:
#one condition doesnot give a true value, will automatically move to next condition.

# RELATIONAL/COMPARISION OPERATOR.
#> -----> GREATER THAN  10>5 TRUE, 10<8 FALSE.
#>= ---->GREATER THAN EQUAL TO 10>=10 TRUE.
#< ----> SMALLER THAN 10<11 TRUE, 10<8 FALSE.
#<= ----> SMALLER THAN EQUALS TO 10<=10 TRUE.
#== ---> EQUALS TO 10==10 TRUE.
#!= ---->NOT EQUALS TO 10!=5 true
# if - else-elif condition:
# = EXAMPLE 1: 
# IF CONDITION 1:
#STATEMENT 1
#ELIF CONDITION 2:
#STATEMENT 2 
#ELIF CONDITION 3:
#STATEMENT 3
#ELSE:
#STATEMENT 4
#JUST LIKE :
#80-100 ==>DISTINCTION
#60-79 ==> FIRST DIVISION
#50-69 ==> SECOMD DIVISION


#EXAMPLE 2:
# age = int(input("Enter your age:"))
# if age <=18:
#     print("You are not eligibile to vote")
# elif:
#     print("You are eligible to vote") 
# else:
#     print("wait when you reach at the age 18")

# NESTED CONDITION:


#TRUTHTABLE:
# 1. AND
#   A                  B                   AND
#O(FALSE)           0(FALSE)             0(FALSE)
#0(FALSE)           1(TRUE)              0(FALSE)
# 1(TRUE)           0(FALSE)             0(FALSE)
# 1(TRUE)           1(TRUE)              1(TRUE)
# AND ==> ALL THE CONDITIONS MUST BE TRUE.

# 2. OR
#   A                  B                    OR
# 0                   0                    0 
# 1                   0                    1
# 0                   1                    1
# 1                   1                    1 

# 3. NOT
# A        B
# 1        0
# 0        1
    


# marks=int(input("enter your marks="))
# if (marks >= 80):
#     print("Distinction")
# elif (marks >= 60):
#     print("First Division")
# elif (marks >= 40):
#     print("Second Divsion")
# elif (marks >= 32):
#     print("Third Division")
# else:
#     print("Fail")

# age = 20
# is_citizen = True
# if age >= 18 and is_citizen:
#     print("You are eligible to vote!!!")

# marks >= 80
# attendence >= 80
# discipline = True
# marks = int(input("Enter your marks"))
# attendence = int(input("Enter your attendence"))

# if not discipline:
#     print("Not Eligible for Scholarship")

# if marks >= 80 and attendence >= 70:
#     print("Scholarship Eligible")
# else: 
#     print("Sorry you are not eligible for Scholarship")

#TASK 1:
# laptop_login = input("Enter login method")
# if laptop_login == "PIN" or laptop_login =="fingerprint":
#     print("Login sucess")
# else:
#     print("Login Failed")

# if payment made via khalti/e-sewa:
#ask user for payment wallet.
# payment_wallet = input("Enter payment wallet")
# if payment_wallet == "khalti" or payment_wallet == "e-sewa":
#     print("Payment accepted")
# else:
#     print("Payment failed")

# age = 20
# is_citizen = True

# if age >= 18:
#     if is_citizen:
#         print("Eligible to vote")

# need atleast 75% attendence.
# fees should be paid
# to sit and take the exam.

attendence = input("Enter your attendence percentage:")
fee = input("Fee is paid:")
if fee == "paid" and attendence >= "75":
    print("you can sit and take the exam")
else:
    print("You have to fulfil the requirement first")




    


