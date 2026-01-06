# Build a File-Based Notes App

filename = "notes.txt"

while True:
    print("\n--- MY NOTES APP ---")
    print("1. View Notes")
    print("2. Add Notes")
    print("3. Exit")

    choice = input("Choose (1/2/3):")

    if choice == "1":

        try:
            with open(filename, "r") as f:
                print("\n" + f.read())
        except FileNotFoundError:
            print("\n No Notes Found")

    elif choice == "2":
        
        note = input("Write your notes: ")
        with open(filename, "a") as f:
            f.write("- " + note + "\n")
        print("Notes Saved!")

    elif choice == "3":

        print("Exiting App....")
        break

    else:
        print("Invalid Choice")
