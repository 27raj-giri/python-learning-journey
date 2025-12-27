dollar = int(input("Enter amount in USD: "))

def convert(usd):
    inr = usd * 90.70
    return inr

print("Amount in INR is:", convert(dollar))