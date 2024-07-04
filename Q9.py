marks = int(input("Enter Student's marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grades = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
    
print("Grade of Students are :" , grade)

# Output

# Enter Student's marks: 74
# Grade of Students are : C

# Enter Student's marks: 99
# Grade of Students are : A

