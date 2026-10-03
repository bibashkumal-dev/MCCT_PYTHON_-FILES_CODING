# 1. USING FOR LOOP.
# for i in range(1, 6):
#     print(f"{'*' * i}")

# var1 = "HELLLO"
# for i in var1:
#     print(i)


#WHILE LOOP: ITERATIVE THE BLOCK OF CODE UNTIL A CONDITION IS TRUE.
#while <condition>:

#example: Print from 1 to 5 using while loop.

# i = 0 
# while i <= 5:
#     print(i)
#     i += 1

# FOR LOOP: LOOP THE SEQUENCE OR NUMBERS .
#WHILE LOOP: LOOP DEPENDS ON CONDITION.

# if password is entered correctly gives the access either
#ask to enter the password.

# password1 = ""
# while password1 != "mypassword":
#     password1 = input("Enter the password: ")
#     if password1 == "mypassword":
#         print("Access granted Sucessfully")
#     else:
#         print("Access denied. Try again.")


# password2 = ""
# while password2 != "BIBASH":
#     password2 = input("Enter the password: ")
#     if password2 == "BIBASH":
#         print("Access granted Sucessfully")
#         break
#     else:
#         print("Access Rejected. Try again.")



# 1 = ouput(hello)
# 2 = output(you pressed 2)
# 3 = output(you pressed 3)
# 4 = output(invalid!)

# num = ""
# while num != "1":
#     num = input("Enter the number: ").split()
#     if num == "1":
#         print("Hello")
#     elif num == "2":
#         print("You pressed 2")
#     elif num == "3":
#         print("You pressed 3")
#     else:
#         print("Invalid!")

# choice  = ""
# while choice != "":
#     print("1. Hello")
#     print("2. You pressed 2")
#     print("3. You pressed 3")   
#     print("4. you pressed 4")
#     print("5. Invalid!")

#     choice = input("Enter the choice: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("You pressed 2")
#     elif choice == "3":
#         print("You pressed 3")
#     elif choice == "4":
#         print("You pressed 4")
#     else:
#         print("Invalid choice. Please try again.")

# HOMEWORK :ATM WITHDRAW MECHANISM same using while loop and if else condition.


# choice = ""

# while choice != "1":
#     print("1. Hello")
#     print("2. You pressed 2")
#     print("3. You pressed 3")
#     print("4. You pressed 4")

#     choice = input("Enter the choice: ")

#     if choice == "1":
#         print("Hello")

#     elif choice == "2":
#         print("You pressed 2")

#     elif choice == "3":
#         print("You pressed 3")

#     elif choice == "4":
#         print("You pressed 4")

#     else:
#         print("Invalid choice. Please try again.")

#BREAK = TO TERMINATE THE INFINITE LOOP.

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

#Continue = TO SKIP THE CURRENT ITERATION AND MOVE TO NEXT ITERATION.
# for i in range(1, 10): 
#     if i == 3:
#         continue
#     print(i)

#NESTED LOOP: LOOP INSIDE ANOTHER LOOP.
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i: {i}, j: {j}")

#HOMEWORK: ATM WITHDRAW MECHANISM USING WHILE LOOP AND IF ELSE CONDITION.

while True:
    print("\nATM")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", 10000)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > 10000:
            print("Insufficient balance!")

        else:
            balance = 10000 - amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)

    elif choice == "3":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice!")
          