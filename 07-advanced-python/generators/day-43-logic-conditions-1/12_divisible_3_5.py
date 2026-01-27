def divisinble_gen(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield i

for num in divisinble_gen(50):
    print(num)