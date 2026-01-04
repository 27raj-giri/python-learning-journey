# Convert all text to Uppercase

with open("info.txt", "r") as f_in, open("upper.txt", "w") as f_out:
    content = f_in.read()       
    f_out.write(content.upper()) 
print("Converted to Uppercase!")