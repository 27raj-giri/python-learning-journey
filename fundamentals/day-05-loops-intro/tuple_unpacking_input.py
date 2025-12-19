name = input("Enter Name = ")
age = int(input("Enter Age = "))
city = input("Enter City = ")

info = (name, age, city)

name = info[0]
age = info[1]
city = info[2]

print(f"{name} from {city} is {age} years old")
