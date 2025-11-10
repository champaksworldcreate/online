a = [7, 5, 1, 8, 5, 9, 5, 2]
# 1,4 and 6
print(a)
searchvalue = int(input("Enter value to search "))
n = len(a)

position = "Not found"
r = range(n-1, -1, -1)
for index in r:

    if a[index] == searchvalue:
        position = index
        print(position)
        break
if position == "Not found":
    print(f"{searchvalue} is {position}")
else:
    print(f"{searchvalue} found at {position}")
