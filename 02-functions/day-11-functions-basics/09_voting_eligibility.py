def eligible(a):
    if a >= 18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"

age = int(input("Enter age: "))
print(eligible(age))
