def recursiveBinarySearch(a, left, right, target):
    
    if left > right:
        return f"{target} not found"
    mid = (left+right)//2
    print(f"{left} to {right}, {a[left:right+1]}, Mid={mid} value={a[mid]}")
    if target == a[mid]:
        return f"{target} found at {mid}"
    if target < a[mid]:
        return recursiveBinarySearch(a, left, mid-1, target)
    else:
        return recursiveBinarySearch(a, mid+1, right, target)


a = [-10, -5, 0, 5, 7, 10]
left, right = 0, len(a)-1
# target = int(input("Enter target\n"))
result = recursiveBinarySearch(a, left, right, int(input("Enter target\n")))
print(a)
print(result)
