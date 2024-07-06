#Dictionary
info = {
    "name" : "Ish",
    "subjects" : ["Java", "Python"],
    "topics" : ("Dictionary", "Sets"),
    "learning" : "Python",
    "age" : 21,
    "is_adult" : True,
    "marks" : 95
}

print(type(info))
print(info["age"])
info["name"] = "Isha"
info["surname"] = "Rani"
print(info)

# Output
# {'name': 'Ish', 'subjects': ['Java', 'Python'], 'topics': ('Dictionary', 'Sets'), 'learning': 'Python', 'age': 21, 'is_adult': True, 'marks': 95}
# <class 'dict'>
# 21
# {'name': 'Isha', 'subjects': ['Java', 'Python'], 'topics': ('Dictionary', 'Sets'), 'learning': 'Python', 'age': 21, 'is_adult': True, 'marks': 95, 'surname': 'Rani'}

#Nested Dictionary
student = {
    "name" : "Rahul Kumar",
    "subjects" : {
        "phy" : 86,
        "chem" : 88,
        "maths" : 87
    } 
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# Output
# {'name': 'Rahul Kumar', 'subjects': {'phy': 86, 'chem': 88, 'maths': 87}}
# {'phy': 86, 'chem': 88, 'maths': 87}
# 88

#Dictionary Methods
#.keys() - returns all keys
print(student.keys())
print(list(student.keys())) #typecast to list
print(len(list(student.keys())))
# Output
# dict_keys(['name', 'subjects'])
# ['name', 'subjects']
# 2

#.values() - returns all values
print(list(student.values()))
# Output
# ['Rahul Kumar', {'phy': 86, 'chem': 88, 'maths': 87}]

#.items() - returns all (key, value) pairs as tuples
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
# Output
# [('name', 'Rahul Kumar'), ('subjects', {'phy': 86, 'chem': 88, 'maths': 87})]
# ('name', 'Rahul Kumar')

#.get("key") - returns the key according to value
print(student["name"])
print(student.get("name"))
# Output
# Rahul Kumar
# Rahul Kumar

#.update() - inserts the specified items to the dictionary
student.update({"city" : "Ranchi"})
print(student)
# Output
# {'name': 'Rahul Kumar', 'subjects': {'phy': 86, 'chem': 88, 'maths': 87}, 'city': 'Ranchi'}