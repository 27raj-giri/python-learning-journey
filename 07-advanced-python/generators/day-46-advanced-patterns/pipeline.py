def number_source(max_num):
    for i in range(max_num):
        yield i 


def filter_evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square_numbers(numbers):
    for n in numbers:
        yield n * n


numbers = number_source(10)
even = filter_evens(numbers)
squared = square_numbers(even)

for s in squared:
    print(s)