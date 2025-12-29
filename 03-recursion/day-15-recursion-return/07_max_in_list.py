# Find maximum element in a list

def maximum(arr):
    if len(arr) == 1:
        return arr[0]
    
    return max(arr[0], maximum(arr[1:]))

print(maximum([9, 18, 5, 27, 14]))
