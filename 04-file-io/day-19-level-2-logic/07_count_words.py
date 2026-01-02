# Count the number of words in a file

with open("data.txt", "r") as f:
    content = f.read()
    words = content.split()

print(words)
print(len(words))