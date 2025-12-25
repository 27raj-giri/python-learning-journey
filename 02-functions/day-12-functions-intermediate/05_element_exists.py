# Write a function that checks if an element exists in a list.

def exists(lst, elem):
    for item in lst:
        if item == elem:
            return True
       
    return False

elements = [9, 18, 27, 5, 14]
target = int(input("Enter the element to search: "))

result = exists(elements, target)
print(f"Element {target} exists in the list: {result}")
    

