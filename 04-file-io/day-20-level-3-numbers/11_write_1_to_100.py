# Write numbers 1 to 100 into a file

with open("num.txt", "w") as f:
    for i in range(1,101):
        f.write(str(i) + "\n")