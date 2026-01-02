# Count the number of lines in a text file

with open("data.txt", "r") as f:
    lines= f.readlines()
    count= len(lines)

print(count)