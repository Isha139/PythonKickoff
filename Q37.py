n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
    
print("Factorial of ", n, "is: ",fact)

# Output
# Enter a number: 5
# Factorial of  5 is:  120