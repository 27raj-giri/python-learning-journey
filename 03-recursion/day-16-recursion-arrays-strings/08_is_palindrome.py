# Check if a string is palindrome

def palindrome(text):
    text = text.lower()
    
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return palindrome(text[1:-1])

    return False

print(palindrome("Noon"))