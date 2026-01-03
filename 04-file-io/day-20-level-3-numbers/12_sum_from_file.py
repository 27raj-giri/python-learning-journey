# Read numbers and calculate their sum

sum = 0

with open("numbers.txt","r") as f:
    for line in f:

        number = int(line.strip())

        sum = sum + number

print(sum)