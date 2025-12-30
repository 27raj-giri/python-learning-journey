# Find LAST occurrence of an element

def last_index(arr, target, index=0, last=-1):
    if index == len(arr):
        return last

    if arr[index] == target:
        last = index

    return last_index(arr, target, index+1, last)

print(last_index([9,18,27,9,4,15], 9))