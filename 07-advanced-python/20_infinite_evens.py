def infinite_even():
    n = 0
    while True:
        yield n 
        n += 2

stream = infinite_even()

for i in range(10):
    print(next(stream))