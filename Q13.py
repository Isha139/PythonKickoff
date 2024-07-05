#Lists
marks = [87, 64, 33, 95, 76]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

# Output
# [87, 64, 33, 95, 76]
# 5
# 87
# 64

Student = ["Karan",18, 85.9, "Delhi"]
print(Student)

#Output
# ['Karan', 18, 85.9, 'Delhi']

str = "Hello"
str[0] = "y"
#Output : Error

# Difference between List and String
Student[0] = "Arjun"
print(Student)
# Output
# ['Arjun', 18, 85.9, 'Delhi']

#List Slicing
print(marks[0:4])
print(marks[0:])
print(marks[:4])
print(marks[-3:-1])

# Output
# [87, 64, 33, 95]
# [87, 64, 33, 95, 76]
# [87, 64, 33, 95]
# [33, 95]

#List Methods
list = [2, 1, 3]
list.append(4)
print(list.sort())
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(1, 5)
print(list)
list.remove(2)
print(list)
list.pop(2)
print(list)

#Output
# None
# [1, 2, 3, 4]
# [4, 3, 2, 1]
# [1, 2, 3, 4]
# [1, 5, 2, 3, 4]
# [1, 5, 3, 4]
# [1, 5, 4]

list2 = ["Banana", "Lichi", "Mango", "Apple"]
list2.sort()
print(list2)
# Output
# ['Apple', 'Banana', 'Lichi', 'Mango']