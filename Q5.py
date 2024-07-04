#String
s1 = "This is a \tString.\nWe are creating python string."
s2 = 'Hello, I am a String'
s3 =  '''Hello '''
s4 = """Hiiee"""
ch = s1[0]

print(s1, "," , s2, ",", s3, ",", s4)
print(s3+s4)
print(len(s3+s4))
print(len(s4))

# Output
# This is a       String.
# We are creating python string. , Hello, I am a String , Hello  , Hiiee
# Hello Hiiee
# 11
# 5

 #-Indexing
print(ch)
print(s2[3])

# Output
# T
# l

#-Slicing
print(s1[0:19])
print(s1[19:]) #[19: len(s1)]
print(s1[:19]) #[0:19]

# Output
# This is a       String.

# We are creating python string.
# This is a       String.

#String Function
s5 = "i am a coder."
print(s5.endswith("er"))
print(s5.capitalize())
print(s5.replace("coder", "student"))
print(s5.find("o"))
print(s5.count("a"))

# Output
# False
# I am a coder.
# i am a student.
# 8
# 2