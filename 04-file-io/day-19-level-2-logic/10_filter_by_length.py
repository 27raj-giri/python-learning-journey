# Print only lines longer than 20 characters

with open("data.txt", "r") as f:
    for line in f:
        if len(line) > 20:
            print((line.strip()))