# Find sum of elements in a list

def sum(arr, idx = 0):
    if idx == len(arr):
        return 0

    return arr[idx] + sum(arr, idx + 1)

print(sum([1, 2, 3]))