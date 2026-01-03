# Separate even and odd numbers into two files

with open("numbers.txt", "r") as f_in, \
     open("even.txt", "w") as f_even, \
     open("odd.txt", "w") as f_odd:
    
    for line in f_in:
        num = int(line.strip())

        if num % 2 == 0:
            f_even.write(str(num) + "\n")
        else:
            f_odd.write(str(num) + "\n")

print("Separation completed")
