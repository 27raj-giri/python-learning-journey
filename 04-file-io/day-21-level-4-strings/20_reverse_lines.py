# Reverse each line

with open("data.txt", "r") as f_in, open("reverse.txt", "w") as f_out:
    for line in f_in:
        clean_line = line.strip()
        reverse = clean_line[::-1]
        f_out.write(reverse + "\n")