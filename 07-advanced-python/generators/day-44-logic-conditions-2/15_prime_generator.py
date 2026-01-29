def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num

print("Prime num up to 30:")
for prime in prime_generator(30):
    print(prime, end=" ")
