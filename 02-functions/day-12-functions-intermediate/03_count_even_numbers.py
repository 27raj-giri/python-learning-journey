# Write a function that counts how many even numbers are in a list.

def count(lst):
    count = 0
    for n in lst:
        if n % 2 == 0:
            count += 1
    return count

num = [12, 7, 9, 18, 27, 33, 44, 25, 60, 14, 5]
print("Count of even numbers:", count(num))
