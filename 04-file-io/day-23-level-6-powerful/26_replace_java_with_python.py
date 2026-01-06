# WAF that replace all occurrences of "java" with "python" in above file.

def replace(filename):
    with open(filename, 'r') as f:
        content = f.read()

    content = content.replace("java", "python")

    with open(filename, "w") as f:
        f.write(content)

replace("sample.txt")