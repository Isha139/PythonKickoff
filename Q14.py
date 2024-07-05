#Tuples
tuple = (2, 1, 3, 1)
print(tuple)
print(type(tuple))
print(tuple[1])

tup = (2,)
print(tup)

# Output
# (2, 1, 3, 1)
# <class 'tuple'>
# 1
# (2,)

#Tuple Slicing
print(tuple[0:3])
# Output
# (2, 1, 3)

#Tuple Method
print(tuple.index(1))
print(tuple.count(1))
# Output
# 1
# 2