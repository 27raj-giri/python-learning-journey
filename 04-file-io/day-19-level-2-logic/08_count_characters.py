# Count how many characters are in a file

with open("data.txt", "r") as f:
    char = f.read()

print(len(char))