tup = (1, 4, 9, 16, 25, 26, 49, 64, 81, 100)
search = int(input("Enter a number to search: "))
for val in tup:
    if search == val:
        print(f"{search} is found in the tuple.")
        break
else:
    print(f"{search} is not found in the tuple.")
    