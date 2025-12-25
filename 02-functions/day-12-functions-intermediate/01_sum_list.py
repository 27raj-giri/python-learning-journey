# Write a function that returns the sum of all elements in a list.

def sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

list = [10, 20, 30, 40, 50]
print("Sum:", sum(list))
