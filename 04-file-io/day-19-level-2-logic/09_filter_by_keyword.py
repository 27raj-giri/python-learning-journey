# Print only lines that contain "I"

with open("data.txt", "r") as f:
    for line in f:
        if "I" in line:
            print(line)