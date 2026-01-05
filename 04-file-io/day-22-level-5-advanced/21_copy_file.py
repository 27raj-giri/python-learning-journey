# Copy content from one file to another

with open("data.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
    