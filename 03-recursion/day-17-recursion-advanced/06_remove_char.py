# Remove all occurrences of a character

def remove(text, char_remove, index = 0, result = ""):
    
    if index == len(text):
        return result

    if text[index] != char_remove:
        result += text[index]

    return remove(text, char_remove, index + 1, result)

print(remove("aayush", "a"))