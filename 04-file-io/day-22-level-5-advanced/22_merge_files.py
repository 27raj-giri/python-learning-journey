# Merge two text files into one

with open("data.txt", "r") as f1, open("input.txt", "r") as f2, open("merge.txt", "w") as out:
    out.write(f1.read())
    out.write("\n")
    out.write(f2.read())
