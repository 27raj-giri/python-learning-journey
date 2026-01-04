# Replace spaces with underscores

with open("input.txt", "r") as f_in, open("output.txt", "w") as f_out:
    content = f_in.read()

    new_content = content.replace(" ", "_")
    f_out.write(new_content)


