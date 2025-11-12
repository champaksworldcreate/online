def iterativeBinarySearch(a, target):
    left, right = 0, len(a)-1
    while True:
        
        mid = (left+right)//2
        # print(f"Left={left}, mid={mid}, right={right}, {a[left:mid]},{a[mid:right]}")
        if target == a[mid]:
            return f"{target} found at {mid}"
        if target < a[mid]:
            right = mid-1
        else:
            left = mid+1
        if left > right:
            return f"{target} not found"


a = [-9, 2, 4, 6, 7, 8, 9, 51]
# target = int(input("Enter the value to search\n"))
for target in a:
    result = iterativeBinarySearch(a, target)
    print(result)
