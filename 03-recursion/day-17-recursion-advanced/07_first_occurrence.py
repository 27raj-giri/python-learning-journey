# Find FIRST occurrence of an element

def find(arr, target, index = 0):

    if index == len(arr):
        return -1

    if arr[index] == target:
        return index

    return find(arr, target, index + 1)

print(find([9, 18, 27, 4, 15, 27], 27))