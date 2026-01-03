# Read numbers and find the maximum

max = -1

with open("numbers.txt", "r") as f:
    for line in f:
        num = int(line.strip())

        if num > max:
            max = num

print(max)