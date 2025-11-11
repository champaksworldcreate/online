a = [7, 5, 1, 8, 5, 9, 5, 2]
print(a)
# a[3]=90
# print(a)
searchvalue=int(input("Enter value to search "))
n=len(a)
# print(f"n={n}")
# print(a[n-1])

position="Not found"
r=range(n)
for index in r:
    # print(index,a[index])
    if a[index]==searchvalue:
        position=index
        break
if position=="Not found":
    print(f"{searchvalue} is {position}")
else:
    print(f"{searchvalue} found at {position}")
