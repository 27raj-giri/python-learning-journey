# Count how many EVEN numbers are in a file

count = 0

with open("numbers.txt", "r") as f:
    for line in f:
        num = int(line.strip())

        if num % 2 == 0:
            count += 1

print(count)
