# Read a CSV-like file and format the output

with open("data.csv", "r") as f:
    for line in f:

        parts = line.strip().split(",")

        name = parts[0]
        age = parts[1]
        city = parts[2]

        print(f"{name:<10} | {age:<5} | {city}")