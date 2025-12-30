# Print all elements of a list

def list(arr, idx=0):
    if idx == len(arr):
        return

    print(arr[idx])

    list(arr, idx + 1)

list([27, 9, 5, 18, 45])