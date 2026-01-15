# Create Phone class. Create Smartphone class that inherits and adds install_app() method.

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Phone):
    def install_app(self, app_name):
        print(f"Installing {app_name}...")

s = Smartphone()
s.make_call()
s.install_app("Whatsapp")
