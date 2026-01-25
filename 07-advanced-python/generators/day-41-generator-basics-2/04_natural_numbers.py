def natural(n):
    num = 1
    while num <= n:
        yield num 
        num += 1

for i in natural(10):
    print(i)
    