def count_to_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = count_to_five()

for num in gen:
    print(num)
