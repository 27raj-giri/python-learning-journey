#Write 5 numbers (1–5) into a file

with open("numbers.txt", "w") as f:
    for i in range(1, 6):
        f.write(str(i) + "\n")
