# Reverse a string using recursion

def reverse(txt, idx = 0):
    if len(txt) == 0:
        return ""

    return txt[-1] + reverse(txt[:-1])

print(reverse("Aayush"))