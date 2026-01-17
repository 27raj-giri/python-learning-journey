# Create Password class that stores password as private __password. Add method to verify password.

class Password:
    def __init__(self, secret):
        self.__password = secret

    def verify(self, input):
        if input == self.__password:
            return True
        else:
            return False
        
p = Password(3984)
print(p.verify("wrongpass"))
print(p.verify(3984))

