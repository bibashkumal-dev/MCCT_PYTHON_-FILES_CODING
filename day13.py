# set1 ={10,10,20,30,40,50}
# set2 = {40,50,60,70,80}
# # 1. find the common element in both set.
# common_element = set1.intersection(set2)
# print(common_element)

# # 2. Find the elements exist in set1 but not in set2.
# difference = set1 - set2
# print(difference)

# list1 = [10,10,20,30,30]
# # 3. Remove the duplicate elements from list1 and convert it to set.
# new_set = set(list1)
# print(new_set)


# Dictionary.
# Elements are organizd and store in the form of key:value
# pair.
# Example:
# student1 ={
#     "name": "Spiderman",
#     "age":21,
#     "Course": "BSC. SE",
#     # "Gender": "Female",

# }

# print(student1["name"])
# student1["name"] = "Ironman" #Acess value using key

# print(student1["name"])

# student1['Gender'] = "Male"  # Adding Value
# print(student1)

# del student1['Gender'] #Removing value
# print(student1)

# # 1. Get()
# print(student1.get("age"))
# print(student1.get("phone", "Not Assigned"))

# # 2. Key and Value.:
# print(student1.keys())
# print(student1.values())

# # print whole dictionary
# print(student1.items())

# for i in student1.keys():
#     print(i)

# for i in student1.values():
#     print(i)

# # together key and value we have to iterate>
# for i,j in student1.items():
#     print(i, ":", j)

# # Update method:
# names = {
#     "name1" : "BIBAAH",
#     "name2" : "Hari",
#     "name3" : "Sita",

# }

# names.update({
#     "name4" : "Hari",
#     "name5" : "Shyam",

# })

# print(names)
# # deleted the certain item using pop and popitem.
# names.pop("name2")
# print(names)

# names.popitem()
# print(names)

# names.clear()

students = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 64,
    "Gita": 92,

}
# print all the students who scored greater than 80.
for i, j  in students.items():
    if j>=80:
        print(i, ":", j)

# calculate the average marks of all students marks.
total = 0
for marks in students.values():
    total = total + marks
average = total/len(students)
print("The average marks is :", average)
