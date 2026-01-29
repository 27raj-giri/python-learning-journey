def million_numbers():
    num = 1

    while num <= 1000000:
        yield num 
        num += 1

gen = million_numbers()

print(next(gen))  # Prints 1
print(next(gen))  # Prints 2
print(next(gen))  # Prints 3
# The other 999,997 numbers don't exist in memory yet!