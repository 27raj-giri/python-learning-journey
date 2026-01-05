# Count "ERROR" in logs

error = 0

with open("server.log", "r") as f:
    for line in f:

        if "ERROR" in line:
            error += 1

print(error)
