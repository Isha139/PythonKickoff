#Sets
collections = {1, 2, 3 , 4,"hello", "world", "hello",8}
print(collections)
print(type(collections))
print(len(collections))
# Output
# {1, 2, 3, 4}
# <class 'set'>
#{1, 2, 3, 4, 'world', 'hello'} unique
#{1, 2, 3, 4, 'hello', 8, 'world'} unordered
#7 Ignored duplicate values

#Empty set
collections1 = set()
print(collections1)
# Output
# set()

#Set Method
#add() - Add an element
collections1.add(1)
collections1.add(2)
collections1.add("Hello")
collections1.add("World")
collections1.add("Hello")
print(collections1)
# Output
# {2, 'World', 'Hello'}

#clear() - empties the set
# collections1.clear()
print(collections1)
#Output
#set()

#pop() - removes a random value

print(collections1.pop())
#Output
#2

#union() - combines both set values and returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
#Output
#{1, 2, 3, 4}

#intersection() - combines common values & return new
print(set1.intersection(set2))
#Output
#{2, 3}