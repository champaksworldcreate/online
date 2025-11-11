a = [7, 5, 1, 8, 5, 9, 5, 2]
# 1,4 and 6
print(a)
searchvalue = int(input("Enter value to search "))
n = len(a)

positions = []
r = range(n-1, -1, -1)
for index in r:

    if a[index] == searchvalue:
        positions.append(n-1-index)
        print(positions)
        # break
        # A1,B2,C3.......X24,Y25,Z26   27-1=26
if len(positions) == 0:
    print(f"{searchvalue} is not found")
else:
    print(f"{searchvalue} found at {positions}")
