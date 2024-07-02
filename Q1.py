#Print Statements
print("Hello World,", "Hi World")
print(54)
print(54+2)

#Variables
name = "Isha" #String
age = 21   #Integer
price = 23.99  #Float

print(name, ",", age, "," , price)
print("My name is : ", name)
print("My age is : ", age)

#Data type
print(type(name))
print(type(age))
print(type(price))

old = True
a = None
print(type(old))
print(type(a))

#Print sum
a = 2
b = 3
sum = a + b
print(sum)

#Operators
x = 3
y = 6

#Arithmetic Operators
print(x - y)
print(x + y)
print(x * y)
print(x / y)
print(x % y) #remainder
print(x ** y) #exponential (a power b)

#Relatonal Operators (return boolean value)
print(x == y)
print(x != y)
print(x >= y)
print(x > y)
print(x <= y)
print(x < y)

#Assignment Operators
x += 10
print("x = ", x)

#Logical Operators (and, or, not)

print(not False)
print(not ( x > y))

val1 = True
val2 = False
val3 = True
print("AND operator: ", val1 and val2)
print("AND operator: ", val1 and val3)

print("OR operator: ", val1 or val2)
print("OR operator: ", val1 or val3)

#Type Conversion
m = float("2")
n = 4.2
print(m + n)

#Inputs
#input("Enter your name: ")
name  = input("Enter your name: ")
print("Welcome: ", name)

age = int(input("Enter your age: "))
print(age)


# Output
# Hello World, Hi World
# 54
# 56
# Isha , 21 , 23.99
# My name is :  Isha
# My age is :  21
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>
# 5
# -3
# 9
# 18
# 0.5
# 3
# 729
# False
# True
# False
# False
# True
# True
# x =  13
# True
# False
# AND operator:  False
# AND operator:  True
# OR operator:  True
# OR operator:  True
# 6.2
# Enter your name: Isha
# Welcome:  Isha
# Enter your age: 21
# 21
