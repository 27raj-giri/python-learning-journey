# Create a Password-Protected File Reader

password = "3984"
user = input("Enter Password: ")

if user == password:
    print("Access Granted")
    print("-" * 30)

    with open("secret_data.txt", "r") as f:
        print(f.read())

else:
    print("Access Denied. Wrong Password.")