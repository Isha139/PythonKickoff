list = [1, 2, 2, 1]
list2 = [1, 2 ,3 ,4]
l = list2.copy()
l.reverse()
if(l == list2):
    print("Is pallindrome.")
else:
    print("Not pallindrome")
#Output
#Not pallindrome.

l = list.copy()
l.reverse()
if(l == list):
    print("Is pallindrome.")
else:
    print("Not pallindrome")
#Output
#Is pallindrome.