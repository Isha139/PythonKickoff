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

#-Indexing
print(ch)
print(s2[3])

#-Slicing
print(s1[0:19])
print(s1[19:]) #[19: len(s1)]
print(s1[:19]) #[0:19]