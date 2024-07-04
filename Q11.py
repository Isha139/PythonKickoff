num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number: "))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num3):
    print(num2)
else:
    print(num3)
    
# Output
# Enter first number:2
# Enter second number:5
# Enter third number: 3
# 5