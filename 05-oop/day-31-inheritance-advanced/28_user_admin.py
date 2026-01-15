# Create User and Admin classes where Admin inherits from User and has additional privileges.

class User:
    def login(self):
        print("User Logged In")

class Admin(User):
    def delete_user(self):
        print("User Deleted (Admin Only)")

a = Admin()
a.login()
a.delete_user()