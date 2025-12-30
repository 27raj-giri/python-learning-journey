# Print list elements in reverse

def list(arr, idx=0):
    if idx == len(arr):
        return

    list(arr, idx + 1)

    print(arr[idx])

list([9, 18, 27, 45])