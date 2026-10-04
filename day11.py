#LIST:
#It is a collection of data having following features.
# a. stored inside square (big) bracket.
# b. can store single or multiples values:
# abc = [1]
# abc = []
# abc = [1, 2, 3]
# c. data is stored in ordered.
# d. dats is changeable.
# e. able to store the duplicate value.
# f. allow multiple data type.
# abc = ["abc", 13, "apple"]
# var1 = ['RAM', 'SHYAM', 'HARI']
# ASSIGNED THE VARIABLE.
# DECLARE THE SQUARE BRACES.
# PUT ELEMENTS(DATA) IN SQUARE BRACKET SEPERATED BY COMMAS.
# EXAMPLE:
# var2 = ["RAM", 20, 50.50, False]
# important: WHAT IS LIST INDEX.
# var2 = ["RAM", 20, 50.50, False]
# # example:
# index(0) = "Ram"
# index(1) = 20
# index(2) = 50.50
# index(3) = False
# Example1:
# name = ["Ram", "Shyam", "Hari", "Sita"]
# print(name[0])
# #  -ve Index in list:
# # start count from right to left:
# name = ["Ram", "Shyam", "Hari", "Sita"]
# print(name[-2])

# Now let's change the value of list:
# superhero = ["Ironman", "Captain_America", "Thor"]
# superhero[-2] = "Spider_Man"
# print(superhero)

#breaking/ slicing list(tukuraune):
# print(superhero[0:2])
# print(superhero[-2::])

# IMPORTANT: METHOD INN LISTS:
# 1. APPEND()--> ADDING VALUE(DATA,ITEM,ELEMENTS) AT THE END.
# superhero = ["Ironman", "Captain_America", "Thor"]
# superhero.append("Bibash")
# superhero.append(["value1, value2"])
# print(superhero)

# 2.extend()
# num1 = [10,20,30]
# num1.extend([50,60])
# num1.extend([80,90])
# print(num1)

# a = ["Apple", 5]
# a.append([10,"Orange"])
# a.extend(["29"])
# print(a)

# # Insert()-->
# names = ["Ram", "Shyam", "Hari"]
# names.insert(1, "Sita")
# print(names)
# # names.insert(index, "new_value")

# # remove()--> it removes the specific value.
# names.remove("Hari")
# print(names)

# # pop(): removes an element, itmes using index.
# names.pop(0)
# print(names)

# # Remove everything from list:
# # clear
# names.clear()
# print(names)

# index ()
# names = ['ram', 'shyam', 'hari', 'sita']
# print(names.index('shyam'))

# num1 = [1,2,1,2,1,2,1,2,1,2,10,5,10]
# print(num1.count(1))
# print(num1.sort())


# num2 = [50,10,20,40,30]
# num2.sort()
# print(num2)
# num2.sort(reverse=True)
# print(num2)

# num3 = [10,20,30,40,50]
# num3.reverse()

# print(num3)
# DIFFERENCE BETWEEN APPEND AND EXTEND ARE:
# APPEND                                        EXTEND:                            INSERT                       REMOVE
# ADD ONLY ONE VALUE                    ADD MULTIPLE VALUE.                 ADD THE VALUES              REMOVE THE VALUE.



# index alwasy start counnt form left to right number count 0 and length always start from 1.
# copy:
a = [10,20,30]
b = a.copy()
print(b)

# replace:
abc = ["a", 'x1', 'Z', 'x', 'x']
abc[1] = 'b'
print(abc)

# length(len):
print(len(abc))

abc = [10,20,30,40,50]
print(max(abc))
print(min(abc))
print(sum(abc))

