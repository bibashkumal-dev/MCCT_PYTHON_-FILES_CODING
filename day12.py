# # find the numbers greater than 10 in a list.
# # num1 = [1,4,6,10,20,21,11,15]
# # for i in num1:
# #     if i > 10:
# #         print(i)


# # while in list:
# num2 = [10,20,30,4,100,8,10,12,50,81]
# i = 0
# while i < len(num2):
#     if num2[i] > len(num2):
#         print(num2[i])
#     i += 1

# # TUPLES:
# #IT IS A COLLECTION OF ITEMS, DATA HAVING FOLLOWING FEATURES:
# # 2. USES SMALL BRACES.(   )
# # 2. IT IS ORDERED AND INDEXED.
# # 3. ITEMS ARE IMMUTABLE; NOT CHANGEABLE.
# # 4. ALLOWS THE ITEMS DUPLICATION.
# # EX: 
# num1 = ("RAM", "Shyam","Someone")
# # list--> mutuable
# # tuples--> immutable.

# num1 = ("RAM", "Shyam", "Someone")
# print(num1[1])
# print(num1[-1])

#  type casting: one datatype to another datatype.
# ex: a=1 b=2 and a=2 b=1
# # counr():
# # index():

# num1 = ("RAM", "Shyam", "Someone")
# num1 = list(num1)
# print(type(num1))

# num1.append("Sita")
# num1=tuple(num1)
# print(type(num1))
# print(num1)

# sets
# does not allow duplicated items.
# can be unordered/ doesnot use indexing.
# items of sets are variable.
# var1 = {10,20,30,40,50}
# var2 = {10,10,20,20,30,40}
# print(var2)

# methods in set:
# 1. add()
set1 = {10,20,30}
set1.add(50)
print(set1)

# 2. copy()
set1.copy()
print(set1)

# 3.remove()
set1.remove(50)
print(set1)

# 4.update()
set1.update()
print(set1)

# 5. pop()
set1.pop()
print(set1)

# 6.issubset()
seta = {1,2,3,4}
setb = {1,2,3,4,5,6}
print(seta.issubset(setb))

# I. SET COMBINE WITH AND, OR, NOT LOGIC OPERATORS IN SET IN VEN DIAGRAM.

# 7.union()
setc = {1,2,5}
setd = {3,4,6}
# (setc)U(setd) = {1,2,3,4,5,6}
print(setc.union(setd))
print(setc|setd)
# 8. symmetric_difference()
# 9.intersection()
# 10.difference()



