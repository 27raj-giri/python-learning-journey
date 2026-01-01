# Read a file and print line by one

with open("numbers.txt", "r") as f:
    for line in f:
        print(line.strip())
        