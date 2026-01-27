def only_positive(numbers):
    for num in numbers:
        if num > 0:
            yield num

nums = [-10, 5, -3, 27, -9, 0, 4, -1]
for p in only_positive(nums):
    print(p)