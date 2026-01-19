# Create Payment class with process() method. Create CreditCard, DebitCard, PayPal classes with different implementations.

class Payment:
    def process(self):
        print("Processing Generic Method")
    
class CreditCard(Payment):
    def process(self):
        print("Processing Credit Card Payment.....")

class PayPal(Payment):
    def process(self):
        print("Processing PayPal Payment....")

def make_payment(method):
    method.process()

c = CreditCard()
p = PayPal()

make_payment(c)
make_payment(p)