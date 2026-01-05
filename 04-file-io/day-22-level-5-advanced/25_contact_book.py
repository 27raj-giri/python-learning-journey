# File-based Contact Book

filename = "contacts.txt"

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter Choice:").strip()

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        f = open(filename, "a")
        f.write(name + " : " + phone + "\n")
        f.close()

        print("Contact Saved")

    elif choice == "2":
        print("\n--- Contact List ---")

        if open (filename, "r"):
            f = open(filename, "r")
            print(f.read())
            f.close()

    elif choice == "3":
        print("GoodBye!")
        break

    else:
        print("Invalid Choice")
        
