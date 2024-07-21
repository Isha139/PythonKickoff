#FOR LOOP
nums = [1, 2, 3, 4, 5]
veggies = ["Potato", "Brinjal", "Capsicum"]
str = "hello"
for val in str:
    print(val)
    
# Output

# 1
# 2
# 3
# 4
# 5

# Potato
# Brinjal
# Capsicum

# h
# e
# l
# l
# o

# FOR LOOP WITH ELSE
for char in str:
    if(char == "s"):
        print("l found")
        break
    print(char)
else:
    print("END")
    
# Output
# h
# e
# l found

# h
# e
# l
# l
# o
# END
    