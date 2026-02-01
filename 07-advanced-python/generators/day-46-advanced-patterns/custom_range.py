def my_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step

for num in my_range(1, 10, 2):
    print(num)