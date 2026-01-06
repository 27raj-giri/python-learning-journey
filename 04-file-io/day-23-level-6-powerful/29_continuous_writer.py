# Write user input continuously (The "Diary" Mode)

print("Type your thoughts here. Type 'exit' to stop")

with open("diary.txt", "a") as f:
    while True:
        text = input("> ")

        if text.lower() == "exit":
            print("Diary Saved. GoodBye!!")
            break

        f.write(text + "\n")