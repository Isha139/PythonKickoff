x = int(input("Enter a number to search: "))
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx = 0

while idx < len(tuple):
    if(tuple[idx] == x):
      print("Found")
      break
    else:
      print("Not Found")
    idx +=1
