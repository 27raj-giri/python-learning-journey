# Count occurrences of an element in a list

def countt(arr, target, index=0, count=0):
    if index == len(arr):
        return count

    if arr[index] == target:
        count += 1

    return countt(arr, target, index+1, count)

print(countt([9, 18, 27, 9, 5, 14], 9))