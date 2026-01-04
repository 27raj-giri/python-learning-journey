# Remove duplicate lines

seen = set()

with open("data.txt", "r") as f_in, open("clean.txt", "w") as f_out:
    for line in f_in:
        if line not in seen:
            seen.add(line)
            f_out.write(line)