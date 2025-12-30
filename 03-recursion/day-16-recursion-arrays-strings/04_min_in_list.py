# Find minimum element using recursion

def minimum(arr):
    if len(arr) == 1:
        return arr[0]

    return min(arr[0], minimum(arr[1:]))

print(minimum([9, 18, 27, 5, 14, 3, 45]))