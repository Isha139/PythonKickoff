#Q. WAF to print the length of a list.(list is the parameter)
# cities = ["Ranchi", "Bhubneswar", "Delhi"]

# def len_list(a):
#     print(len(a))
    
# len_list(cities)

# Output
# 3

#Q. WAF to print the elements of a list in a single line.(list is the parameter)

heroes = ["Thor,", "Captain America,", "Ironman,", "Spiderman"]

# def print_hero(a):
#     for i in a:
#       print(i, end=" ")
    
# print_hero(heroes)

# Output
# Thor, Captain America, Ironman, Spiderman

# Q. WAF to find the factorial of n. (n is the parameter)
# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     print(f)
    
# n = int(input("Enter a number: "))
# fact(n)

# Output
# Enter a number: 5
# 120

#Q. WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR")
    
converter(1)

# Output
# 1 USD =  83 INR