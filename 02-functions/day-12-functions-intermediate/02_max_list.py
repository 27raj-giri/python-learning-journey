# Write a function that returns the maximum element in a list.

def max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

list = [27, 9 , 18, 45, 7]
print("Maximum:", max(list))
